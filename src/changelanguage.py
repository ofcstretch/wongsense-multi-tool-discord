import aiohttp
import asyncio
import time
import aiofiles
from style.clear import clear
from style.logo import logo

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
t = time.strftime('%H:%M:%S')

async def change_language():
    await clear()
    await logo()
    print(f"                                     {d}[{rs}1.{d}]{rs} English")
    print(f"                                     {d}[{rs}2.{d}]{rs} Spanish")
    print(f"                                     {d}[{rs}3.{d}]{rs} French")
    print(f"                                     {d}[{rs}4.{d}]{rs} German")
    print(f"                                     {d}[{rs}5.{d}]{rs} Italian")
    print(f"                                     {d}[{rs}6.{d}]{rs} Portuguese")
    print(f"                                     {d}[{rs}7.{d}]{rs} Russian")
    print(f"                                     {d}[{rs}8.{d}]{rs} Japanese")
    print(f"                                     {d}[{rs}9.{d}]{rs} Chinese")
    print(f"                                     {d}[{rs}10.{d}]{rs} Korean")
    choice = input(f"                                     {d}[{rs}Choose language number{d}]{rs} > ")
    language_map = {
        '1': 'en-US',
        '2': 'es-ES',
        '3': 'fr-FR',
        '4': 'de-DE',
        '5': 'it-IT',
        '6': 'pt-PT',
        '7': 'ru-RU',
        '8': 'ja-JP',
        '9': 'zh-CN',
        '10': 'ko-KR'
    }
    language = language_map.get(choice)
    if not language:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Invalid choice. {r}[FAILURE]{rs}")
        return
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]
    async def update_language(token):
        url = 'https://discord.com/api/v10/users/@me/settings'
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        payload = {
            'locale': language
        }
        await clear()
        await logo()
        async with aiohttp.ClientSession() as session:
            async with session.patch(url, headers=headers, json=payload) as response:
                if response.status == 200:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Language updated to: '{language}' {g}[SUCCESS]{rs} ")
                else:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Error updating language {response.status} - {await response.text()} {r}[FAILURE]{rs}")
    tasks = [update_language(token) for token in tokens]
    await asyncio.gather(*tasks)
