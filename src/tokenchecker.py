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

async def token_checker():
    await clear()
    await logo()

    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]

    valid_count = 0
    invalid_count = 0
    flagged_count = 0

    for token in tokens:
        url = 'https://discord.com/api/v10/users/@me'
        headers = {
            'Authorization': token
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            username = data['username']
            discriminator = data['discriminator']
            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Token: {token} | User: {username}#{discriminator} {g}[VALID]{rs}")
            valid_count += 1
        elif response.status_code == 401:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Token: {token} {r}[INVALID]{rs}")
            invalid_count += 1
        else:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {y}[!]{rs} Token: {token} {y}[FLAGGED]{rs}")
            flagged_count += 1

    input(f"                                     {d}[{rs}{t}{d}]{rs} Press Enter to see the results")

    await clear()
    await logo()
    print(f"                                     {d}[{rs}{t}{d}]{rs} {d}[{rs}RESULTS{d}]{rs} > ")
    print(f"                                     {d}[{rs}{t}{d}]{rs} {d}[{rs}Valid Tokens{d}]{rs}   > {valid_count} {g}[SUCCESS]{rs}")
    print(f"                                     {d}[{rs}{t}{d}]{rs} {d}[{rs}Invalid Tokens{d}]{rs} > {invalid_count} {r}[FAILURE]{rs}")
    print(f"                                     {d}[{rs}{t}{d}]{rs} {d}[{rs}Flagged Tokens{d}]{rs} > {flagged_count} {y}[WARNING]{rs}")