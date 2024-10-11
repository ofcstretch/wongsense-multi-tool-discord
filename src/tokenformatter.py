import requests
import json
import time
from style.logo import logo
from style.clear import clear

t = time.strftime('%H:%M:%S')

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def tokenformatter():
    await clear()
    await logo()
    email = input(f"                                     {d}[{rs}Email{d}]{rs} > ")
    password = input(f"                                     {d}[{rs}Password{d}]{rs} > ")
    url = 'https://discord.com/api/v10/auth/login'
    payload = {
        'email': email,
        'password': password
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        data = response.json()
        token = data.get('token')
        if token:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} {token} {g}[SUCCESS]{rs}")
            return format_token(token)
        else:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Token not found in the response. {r}[FAILURE]{rs}")
    else:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Error: {response.status_code} - {response.text} {r}[FAILURE]{rs}")

def format_token(token):
    formatted_token = token.strip()
    return formatted_token