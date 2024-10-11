import requests
import time
import asyncio
import aiofiles
from style.clear import clear
from style.logo import logo

t = time.strftime('%H:%M:%S')

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def webhook_spammer():
    await clear()
    await logo()
    
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]

    if not tokens:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} No tokens available {r}[FAILURE]{rs}")
        return

    webhook_url = input(f"                                     {d}[{rs}Webhook URL{d}]{rs} > ")
    message_content = input(f"                                     {d}[{rs}Message Content{d}]{rs} > ")

    try:
        num_messages = int(input(f"                                     {d}[{rs}Number of Messages{d}]{rs} > "))
    except ValueError:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Invalid number of messages {r}[FAILURE]{rs}")
        return

    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'content': message_content,
        'username': 'Webhook Spammer'
    }

    tasks = []  
    for token in tokens:
        for _ in range(num_messages):
            task = asyncio.create_task(send_message(webhook_url, data, headers, token))
            tasks.append(task)

    await asyncio.gather(*tasks)
    
    print(f"                                     {d}[{rs}{t}{d}]{rs} {y}[+]{rs} Webhook spamming completed {g}[SUCCESS]{rs}")

async def send_message(webhook_url, data, headers, token):
    response = requests.post(webhook_url, json=data, headers=headers)
    if response.status_code == 204:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Message sent successfully to webhook {g}[SUCCESS]{rs}")
    else:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to send message to webhook {r}[FAILURE]{rs}")
    await asyncio.sleep(0.5)

