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
y = "\033[0;33m"

async def channel_spammer():
    await clear()
    await logo()
    channel_id = input(f"                                     {d}[{rs}Channel ID{d}]{rs} > ")
    message = input(f"                                     {d}[{rs}Message Content{d}]{rs} > ")
    message_count = int(input(f"                                     {d}[{rs}How many Messages{d}]{rs} > "))
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    async def send_message(token):
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        headers = {'Authorization': token}
        async with aiohttp.ClientSession() as session:
            for _ in range(message_count):
                for msg in message.split('\n'): 
                    data = {'content': msg}
                    async with session.post(url, json=data, headers=headers) as response:
                        if response.status == 200:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Message sent in {channel_id} {g}[SUCCESS]{rs}")
                        elif response.status == 403:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs}  {r}[INVALID TOKEN]{rs}")
                        else:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to send message {r}[FAILURE]{rs}  {d}[{rs}{response.status}{d}]{rs}")
    tasks = [send_message(token) for token in tokens]
    await asyncio.gather(*tasks)
