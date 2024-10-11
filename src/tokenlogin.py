import requests
import random
import time
from style.clear import clear
from style.logo import logo

t = time.strftime('%H:%M:%S')

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def token_login():
    await clear()
    await logo()
    print(f"                                     {d}[{rs}Enter your token to login:{d}]{rs}")
    token = input(f"                                     {d}[{rs}Token{d}]{rs} > ")
    login_url = "https://discord.com/login"  
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    try:
        print(f"                                     {d}[{rs}{t}{d}]{rs} Attempting login")
        response = requests.get(login_url, headers=headers)
        if response.status_code == 200:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Login {g}[SUCCESS]{rs}")
        else:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-] Login {r}[FAILED]{rs}")
            print(f"                                     {d}[{rs}Error Code:{d}]{rs} {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-] Network Error {r}[FAILED]{rs}")
        print(f"                                     {d}[{rs}Exception:{d}]{rs} {e}")
