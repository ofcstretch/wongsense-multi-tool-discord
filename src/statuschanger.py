import requests
import time
import asyncio
import aiofiles
from pystyle import *
from style.clear import clear
from style.logo import logo

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"

t = time.strftime('%H:%M:%S')

async def change_status():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    if not tokens:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} No tokens available in the file {r}[FAILURE]{rs}")
        return

    print(f"                                     {d}[{rs}Choose your status{d}]{rs} > ")
    print(f"                                     {d}[{rs}1.{d}]{rs} Online")
    print(f"                                     {d}[{rs}2.{d}]{rs} Idle")
    print(f"                                     {d}[{rs}3.{d}]{rs} Do Not Disturb (DND)")
    print(f"                                     {d}[{rs}4.{d}]{rs} Invisible")

    choice = input(f"                                     {d}[{rs}Choose status number{d}]{rs} > ")

    status_map = {
        '1': 'online',
        '2': 'idle',
        '3': 'dnd',
        '4': 'invisible'
    }

    status = status_map.get(choice)

    if not status:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Invalid choice. {r}[FAILURE]{rs}")
        return

    status_message = input(f"                                     {d}[{rs}Custom Status Message (or leave empty){d}]{rs} > ")
    url = 'https://discord.com/api/v10/users/@me/settings'
    await clear()
    await logo()
    for token in tokens:
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        payload = {
            'status': status,
            'custom_status': {
                'text': status_message if status_message else None,
                'expires_at': None
            }
        }
        response = requests.patch(url, headers=headers, json=payload)        
        if response.status_code == 200:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Status updated to: '{status}' with message: '{status_message}' {g}[SUCCESS]{rs} {d}[{rs}{response.status_code}{d}]{rs}")
        else:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Error updating status: {response.status_code} - {response.text} {r}[FAILURE]{rs} {d}[{rs}{response.status_code}{d}]{rs}")