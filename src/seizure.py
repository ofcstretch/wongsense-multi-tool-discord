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

async def seizure():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    try:
        toggle_count = int(input(f"                                     {d}[{rs}Amount of seizure{d}]{rs} > "))
    except ValueError:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Invalid input {r}[FAILURE]{rs}")
        return
    url = 'https://discord.com/api/v10/users/@me/settings'
    for token in tokens:
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        for _ in range(toggle_count):
            for theme in ['dark', 'light']:
                response = requests.patch(url, headers=headers, json={'theme': theme})
                if response.status_code == 200:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Theme changed to {theme} successfully {g}[SUCCESS]{rs}")
                else:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to change theme: {response.text} {r}[FAILURE]{rs}")
                
                await asyncio.sleep(0.3)  
    print(f"                                     {d}[{rs}{t}{d}]{rs} {y}[+]{rs} Seizure completed {g}[SUCCESS]{rs}")