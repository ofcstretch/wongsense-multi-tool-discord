import aiohttp
import time
import aiofiles
import asyncio
from style.logo import logo
from style.clear import clear

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def get_guilds():
    await clear()
    await logo()

    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    t = time.strftime('%H:%M:%S')
    if not tokens:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} No tokens found in the file {r}[FAILURE]{rs}")
        return
    for token in tokens:
        url = "https://discord.com/api/v10/users/@me/guilds"
        headers = {
            "Authorization": f'{token}'
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    guilds = await response.json()
                    if guilds:
                        print(f"                                     {d}[{rs}{t}{d}]{rs} Guilds Found: {g}[SUCCESS]{rs}")
                        for guild in guilds:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} - {guild['name']} (ID: {guild['id']}) {g}[SUCCESS]{rs}")
                    else:
                        print(f"                                     {d}[{rs}{t}{d}]{rs} No Guilds Found {r}[FAILURE]{rs}")
                else:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} Invalid Token or Error Retrieving Guilds {r}[FAILURE]{rs}")