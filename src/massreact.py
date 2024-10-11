import requests
import time
import aiofiles
import asyncio
from pystyle import *
from style.clear import clear
from style.logo import logo

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"

t = time.strftime('%H:%M:%S')

emojis = ['😂', '🔥', '😍', '😎', '💀', '👍', '🎉', '💯', '👀', '👌', '👏', '😡', '🤔', '🙌']

async def mass_react():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    channel_id = input(f"                                     {d}[{rs}Channel ID{d}]{rs} > ")
    message_id = input(f"                                     {d}[{rs}Message ID{d}]{rs} > ")
    for token in tokens:
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        for emoji in emojis:
            emoji_encoded = requests.utils.quote(emoji)  

            reaction_response = requests.put(
                f"https://discord.com/api/v10/channels/{channel_id}/messages/{message_id}/reactions/{emoji_encoded}/@me",
                headers=headers
            )
            if reaction_response.status_code == 204:
                print(f"                                     {d}[{rs}{t}{d}]{rs} Added reaction {emoji} to message {message_id} {g}[SUCCESS]{rs}")
            else:
                print(f"                                     {d}[{rs}{t}{d}]{rs} Failed to react with {emoji} on message {message_id}. Status Code: {reaction_response.status_code} {r}[FAILURE]{rs}")

            await asyncio.sleep(1) 