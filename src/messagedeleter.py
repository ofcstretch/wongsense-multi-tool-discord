import aiohttp
import asyncio
import time
import aiofiles
from style.clear import clear
from style.logo import logo

t = time.strftime('%H:%M:%S')
rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def delete_messages():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    channel_id = input(f"                                     {d}[{rs}Enter the channel ID{d}]{rs} > ")
    url = f'https://discord.com/api/v10/channels/{channel_id}/messages'

    for token in tokens:
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        try:
            async with aiohttp.ClientSession() as session:  
                while True:
                    async with session.get(url, headers=headers) as response:
                        if response.status == 200:
                            messages = await response.json()
                            if not messages:
                                print(f"                                     {d}[{rs}{t}{d}]{rs} {y}[+]{rs} Deleted every message in {channel_id} {g}[SUCCESS]{rs}")
                                break
                            
                            for message in messages:
                                delete_url = f'{url}/{message["id"]}'
                                async with session.delete(delete_url, headers=headers) as delete_response:
                                    if delete_response.status == 204:
                                        print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Deleted message {message['id']} {g}[SUCCESS]{rs}")
                                    else:
                                        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to delete message {message['id']} {r}[FAILURE]{rs}")
                        else:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to fetch messages: {await response.text()} {r}[FAILURE]{rs}")
                            break
        except Exception as e:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} An error occurred: {str(e)} {r}[FAILURE]{rs}")