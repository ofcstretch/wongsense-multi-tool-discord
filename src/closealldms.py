import aiohttp
import asyncio
import time
import aiofiles
from style.logo import logo
from style.clear import clear

t = time.strftime('%H:%M:%S')

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[33m"

async def close_all_dms():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]

    async def close_dm(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        url = 'https://discord.com/api/v9/users/@me/channels'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    channels = await response.json()
                    for channel in channels:
                        channel_id = channel['id']
                        if channel['type'] == 1:  
                            delete_url = f'https://discord.com/api/v9/channels/{channel_id}'
                            async with session.delete(delete_url, headers=headers) as delete_response:
                                if delete_response.status == 204:
                                    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Closed DM: {channel_id} {g}[SUCCESS]{rs}")
                                elif delete_response.status == 404:
                                    print(f"                                     {d}[{rs}{t}{d}]{rs} {y}[-]{rs} DM already closed or does not exist: {channel_id} {y}[SKIPPED]{rs}")
                                else:
                                    error_message = await delete_response.json()
                                    print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to close DM: {channel_id} {r}[FAILURE]{rs} {d}[{rs}{delete_response.status}{d}]{rs} - {error_message.get('message', 'No error message available')}")
                        else:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {y}[-]{rs} Skipped Group/Unsupported Channel: {channel_id} {y}[SKIPPED]{rs}")
                else:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to fetch channels {r}[FAILURE]{rs} {d}[{rs}{response.status}{d}]{rs}")

    tasks = [close_dm(token) for token in tokens]
    await asyncio.gather(*tasks)
