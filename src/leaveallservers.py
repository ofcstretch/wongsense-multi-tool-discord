import httpx
import asyncio
import aiofiles
import time
from style.logo import logo
from style.clear import clear

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def leave_all_servers():
    await clear()
    await logo()
    
    async with httpx.AsyncClient() as client:
        async with aiofiles.open('utils/tokens.txt', 'r') as file:
            tokens = [line.strip() for line in await file.readlines() if line.strip()]
        
        for token in tokens:
            guilds_response = await client.get("https://discord.com/api/v10/users/@me/guilds", headers={"Authorization": token})
            if guilds_response.status_code != 200:
                print(f"                                     {d}[{rs}{t}{d}]{rs} Error fetching guilds Status Code: {guilds_response.status_code} {r}[FAILURE]{rs}")
                continue

            guilds = guilds_response.json()
            if not guilds:
                print(f"                                     {d}[{rs}{t}{d}]{rs} No available guilds to leave {r}[FAILURE]{rs}")
                continue

            for guild in guilds:
                t = time.strftime('%H:%M:%S')
                if guild['owner']:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} owned guild: {guild['name']} ({guild['id']}) {y}[SKIPPED]{rs}")
                    continue

                while True:
                    leave_response = await client.delete(f"https://discord.com/api/v10/users/@me/guilds/{guild['id']}", headers={"Authorization": token})
                    t = time.strftime('%H:%M:%S')
                    if leave_response.status_code == 204:
                        print(f"                                     {d}[{rs}{t}{d}]{rs} Successfully left guild: {guild['name']} ({guild['id']}){g}[SUCCESS]{rs}")
                        break
                    elif leave_response.status_code == 429:
                        retry_after = leave_response.json().get("retry_after", 1)
                        print(f"                                     {d}[{rs}{t}{d}]{rs} Rate limited! Retrying after {retry_after} seconds{r}[FAILURE]{rs}")
                        await asyncio.sleep(retry_after)
                    else:
                        print(f"                                     {d}[{rs}{t}{d}]{rs} Error leaving guild: {guild['name']} ({guild['id']}){r}[FAILURE]{rs}")
                        print(f"                                     {d}[{rs}{t}{d}]{rs} Status Code: {leave_response.status_code} {r}[FAILURE]{rs}")
                        print(f"                                     {d}[{rs}{t}{d}]{rs} Response: {leave_response.text} {r}[FAILURE]{rs}")
                        break

                await asyncio.sleep(1)