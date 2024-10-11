import requests
import time
import asyncio
import aiofiles
from style.clear import clear
from style.logo import logo

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"

t = time.strftime('%H:%M:%S')

async def serverdisplaychanger():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    guild_id = input(f"                                     {d}[{rs}Guild ID{d}]{rs} > ")
    new_nickname = input(f"                                     {d}[{rs}New Nickname{d}]{rs} > ")
    payload = {"nick": new_nickname}
    for token in tokens:
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        
        response = requests.patch(
            f"https://discord.com/api/v10/guilds/{guild_id}/members/@me",
            headers=headers,
            json=payload
        )
        status_code = response.status_code
        if response.status_code == 200:
            await clear()
            await logo()
            print(f"                                     {d}[{rs}{t}{d}]{rs} Changed nickname to {new_nickname} in server {guild_id} {g}[SUCCESS]{rs} {d}[{rs}{status_code}{d}]{rs}")
        else:
            print(f"                                     {d}[{rs}{t}{d}]{rs} Failed to change nickname. {r}[FAILURE]{rs} {d}[{rs}{status_code}{d}]{rs} ")