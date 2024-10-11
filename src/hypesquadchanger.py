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

async def change_hypesquad():
    await clear()
    await logo()
    print(f"                                     {d}[{rs}Choose your HypeSquad House{d}]{rs}: ")
    print(f"                                     {d}[{rs}1.{d}]{rs} Bravery")
    print(f"                                     {d}[{rs}2.{d}]{rs} Brilliance")
    print(f"                                     {d}[{rs}3.{d}]{rs} Balance")
    
    choice = input(f"                                     {d}[{rs}Choose house number{d}]{rs} > ")
    house_map = {
        '1': 1,
        '2': 2,
        '3': 3
    }
    house_id = house_map.get(choice)
    if not house_id:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Invalid choice. {r}[FAILURE]{rs}")
        return
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    async def change_hypesquad_for_token(token):
        url = 'https://discord.com/api/v10/hypesquad/online'
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        payload = {
            'house_id': house_id
        }
        await clear()
        await logo()
        async with aiohttp.ClientSession() as session:
            response = await session.post(url, headers=headers, json=payload)
            if response.status == 204:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} HypeSquad House changed to {choice} {g}[SUCCESS]{rs}")
            elif response.status == 400:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Bad request {r}[FAILURE]{rs}")
            elif response.status == 401:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Unauthorized {r}[FAILURE]{rs}")
            elif response.status == 403:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Forbidden {r}[FAILURE]{rs}")
            elif response.status == 404:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Not Found {r}[FAILURE]{rs}")
            else:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Unexpected error  {response.status} {r}[FAILURE]{rs}")
    tasks = [change_hypesquad_for_token(token) for token in tokens]
    await asyncio.gather(*tasks)