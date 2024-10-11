import requests
import time
import asyncio
import aiofiles
from style.logo import logo
from style.clear import clear

t = time.strftime('%H:%M:%S')

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def thread_messager(token, channel_id, thread_name, message):
    url = f'https://discord.com/api/v9/channels/{channel_id}/threads'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    
    data = {
        'name': thread_name,
        'auto_archive_duration': 60,
        'type': 11
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        thread_id = response.json()['id']
        print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Thread created: {thread_name} {g}[SUCCESS]{rs}")

        message_data = {'content': message}
        message_url = f'https://discord.com/api/v9/channels/{thread_id}/messages'
        msg_response = requests.post(message_url, headers=headers, json=message_data)

        if msg_response.status_code == 200:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Message sent in thread: {thread_name} {g}[SUCCESS]{rs}")
        else:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to send message in thread {r}[FAILURE]{rs}  {d}[{rs}{response.status_code}{d}]{rs}")
    else:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to create thread {r}[FAILURE]{rs} {d}[{rs}{response.status_code}{d}]{rs}")

async def thread_spammer():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    if not tokens:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} No tokens available in the file {r}[FAILURE]{rs}")
        return
    channel_id = input(f"                                     {d}[{rs}Channel ID{d}]{rs} > ")
    thread_name = input(f"                                     {d}[{rs}Thread Name{d}]{rs} > ")
    message = input(f"                                     {d}[{rs}Message Content{d}]{rs} > ")
    count = int(input(f"                                     {d}[{rs}Number of Threads{d}]{rs} > "))
    tasks = []
    for token in tokens:
        for _ in range(count):
            task = thread_messager(token, channel_id, thread_name, message)
            tasks.append(task)

    await asyncio.gather(*tasks)