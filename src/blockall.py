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
y = "\033[33m" 

async def block_everyone():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    async def block_user(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        url = 'https://discord.com/api/v9/users/@me/relationships'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    relationships = await response.json()
                    for relationship in relationships:
                        user_id = relationship['id']
                        relationship_type = relationship['type']
                        if relationship_type in [1, 3]:  
                            block_url = f'https://discord.com/api/v9/users/@me/relationships/{user_id}'
                            block_data = {"type": 2}  
                            async with session.put(block_url, headers=headers, json=block_data) as block_response:
                                if block_response.status == 204:
                                    if relationship_type == 1:
                                        print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Blocked Friend: {user_id} {g}[SUCCESS]{rs}")
                                    elif relationship_type == 3:
                                        print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Blocked Incoming Request: {user_id} {g}[SUCCESS]{rs}")
                                else:
                                    print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to Block User: {user_id} {r}[FAILURE]{rs} {d}[{rs}{block_response.status}{d}]{rs}")
                        else:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {y}[-]{rs} Skipped User: {user_id} (Relationship Type: {relationship_type}) {y}[SKIPPED]{rs}")
                else:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to fetch relationships {r}[FAILURE]{rs} [{response.status}]")
    tasks = [block_user(token) for token in tokens]
    await asyncio.gather(*tasks)
