import aiohttp
import asyncio
import time
import aiofiles
from style.logo import logo
from style.clear import clear

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"

t = time.strftime('%H:%M:%S')

async def fake_typing():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    channel_id = input(f"                                     {d}[{rs}Channel ID{d}]{rs} > ")
    typing_duration = int(input(f"                                     {d}[{rs}Typing Duration (seconds){d}]{rs} > "))
    async def simulate_typing(token):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        print(f"                                     {d}[{rs}{t}{d}]{rs} Simulating typing for {typing_duration} seconds {g}[START]{rs}")
        async with aiohttp.ClientSession() as session:
            for _ in range(typing_duration):
                typing_response = await session.post(
                    f"https://discord.com/api/v10/channels/{channel_id}/typing",
                    headers=headers
                )
                if typing_response.status == 204:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} Typing event sent {g}[SUCCESS]{rs}")
                else:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} Failed to send typing event. Status Code: {typing_response.status} {r}[FAILURE]{rs}")
                await asyncio.sleep(1) 
        print(f"                                     {d}[{rs}{t}{d}]{rs} Finished typing simulation {g}[END]{rs}")
    tasks = [simulate_typing(token) for token in tokens]
    await asyncio.gather(*tasks)