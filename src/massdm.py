import httpx
import asyncio
from style.logo import logo
from style.clear import clear
import time
import aiofiles

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def massdm():
    await clear()
    await logo()
    message = input(f"                                     {d}[{rs}Enter the message to send:{d}]{rs} > ")
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    async with httpx.AsyncClient() as client:
        for token in tokens:
            headers = {
                "Authorization": token,
                "Content-Type": "application/json"
            }
            response = await client.get("https://discord.com/api/v10/users/@me/channels", headers=headers)
            t = time.strftime('%H:%M:%S')
            if response.status_code != 200:
                print(f"                                     {d}[{rs}{t}{d}]{rs} Error fetching DMs Status Code: {response.status_code} {r}[FAILURE]{rs}")
                continue
            await clear()
            await logo()
            dms = response.json()
            for dm in dms:
                if dm.get('last_message_id') is not None:
                    channel_id = dm['id']
                    dm_response = await client.post(
                        f"https://discord.com/api/v10/channels/{channel_id}/messages",
                        headers=headers,
                        json={"content": message}
                    )
                    if dm_response.status_code == 200:
                        print(f"                                     {d}[{rs}{t}{d}]{rs} Message sent to DM: {channel_id} {g}[SUCCESS]{rs}")
                    else:
                        print(f"                                     {d}[{rs}{t}{d}]{rs} Error sending message to {channel_id} Status Code: {dm_response.status_code} {r}[FAILURE]{rs}")
                else:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} Skipping closed DM: {dm['id']} {y}[SKIPPED]{rs}")
            await asyncio.sleep(1)  