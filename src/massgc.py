import requests
import time
import aiofiles
import asyncio
from style.clear import clear
from style.logo import logo

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"

t = time.strftime('%H:%M:%S')

async def massgc():
    await clear()
    await logo()
    user_ids = input(f"                                     {d}[{rs}User IDs{d}]{rs} {d}({rs}comma-separated{d}){rs} > ")
    recipients = [user_id.strip() for user_id in user_ids.split(",")]
    if len(recipients) < 2:
        print(f"                                     {d}[{rs}{t}{rs}]{rs} Error: Group Chats must have at least 2 recipients. {r}[FAILURE]{rs}")
        return
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]

    num_gc = int(input(f"                                     {d}[{rs}Amount of GCs{d}]{rs} > "))
    message = input(f"                                     {d}[{rs}Message content{d}]{rs} > ")

    for token in tokens:
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        
        for _ in range(num_gc):
            create_gc_response = requests.post(
                "https://discord.com/api/v10/users/@me/channels",
                headers=headers,
                json={"recipients": recipients}
            )

            t = time.strftime('%H:%M:%S') 
            if create_gc_response.status_code == 200:
                gc_id = create_gc_response.json()['id']
                await clear()
                await logo()
                print(f"                                     {d}[{rs}{t}{d}]{rs} Created GC with ID: {gc_id} {g}[SUCCESS]{rs}")
                message_response = requests.post(
                    f"https://discord.com/api/v10/channels/{gc_id}/messages",
                    headers=headers,
                    json={"content": message}
                )
                if message_response.status_code == 200:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} Message sent in GC: {gc_id} {g}[SUCCESS]{rs}")
                else:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} Error sending message in GC {gc_id}! Status Code: {message_response.status_code} {r}[FAILURE]{rs}")
            else:
                if create_gc_response.status_code == 403:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} Error: You are not friends with some of the provided User IDs. Can't create GC! {r}[FAILURE]{rs}")
                else:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} Error creating GC! Status Code: {create_gc_response.status_code} {r}[FAILURE]{rs}")