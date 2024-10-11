import requests
import json
import time
import asyncio
import aiofiles
from datetime import datetime
from style.clear import clear
from style.logo import logo

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

t = time.strftime('%H:%M:%S')

async def server_info():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    if not tokens:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} No tokens available in the file {r}[FAILURE]{rs}")
        return
    webhook_url = input(f"                                     {d}[{rs}Webhook URL{d}]{rs} > ")
    guild_id = input(f"                                     {d}[{rs}Guild ID{d}]{rs} > ")
    guild_url = f'https://discord.com/api/v10/guilds/{guild_id}?with_counts=true'
    for token in tokens:
        headers = {
            'Authorization': token.strip()  
        }
        guild_response = requests.get(guild_url, headers=headers)
        status_code = guild_response.status_code  
        if status_code == 200:
            guild = guild_response.json()
            guild_name = guild['name']
            member_count = guild.get('approximate_member_count', 'N/A')
            owner_id = guild.get('owner_id', 'N/A')
            creation_time = (int(guild_id) >> 22) + 1420070400000
            creation_date = datetime.utcfromtimestamp(creation_time / 1000).strftime('%Y-%m-%d %H:%M:%S')
            channels_url = f'https://discord.com/api/v10/guilds/{guild_id}/channels'
            channels_response = requests.get(channels_url, headers=headers)
            channels = channels_response.json() if channels_response.status_code == 200 else []
            total_channels = len(channels)
            voice_channels = len([channel for channel in channels if channel['type'] == 2]) 
            roles_url = f'https://discord.com/api/v10/guilds/{guild_id}/roles'
            roles_response = requests.get(roles_url, headers=headers)
            roles = roles_response.json() if roles_response.status_code == 200 else []
            total_roles = len(roles)

            data = {
                "content": f"```Server Information:\n"
                           f"Server: {guild_name}\n"
                           f"ID: {guild_id}\n"
                           f"Members: {member_count}\n"
                           f"Owner ID: {owner_id}\n"
                           f"Created At: {creation_date}\n"
                           f"Total Channels: {total_channels}\n"
                           f"Voice Channels: {voice_channels}\n"
                           f"Total Roles: {total_roles}\n"
                           f"```",
                "username": "Wongsense"
            }
            webhook_response = requests.post(webhook_url, json=data)
            await clear()
            await logo()
            if webhook_response.status_code == 204:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Server information successfully sent to webhook {g}[SUCCESS]{rs} {d}[{rs}{webhook_response.status_code}{d}]{rs}")
            else:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to send server information {r}[FAILURE]{rs} {d}[{rs}{webhook_response.status_code}{d}]{rs}")
        elif status_code == 403:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Forbidden: You do not have access to this server {r}[FAILURE]{rs} {d}[{rs}{status_code}{d}]{rs}")
        else:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to retrieve server. Token may be invalid or guild ID incorrect {r}[FAILURE]{rs} {d}[{rs}{status_code}{d}]{rs}")