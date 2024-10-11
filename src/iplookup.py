import requests
import time
import asyncio
from style.clear import clear
from style.logo import logo

t = time.strftime('%H:%M:%S')
rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def ip_lookup():
    await clear()
    await logo()
    ip_address = input(f"                                     {d}[{rs}Ip to lookup{d}]{rs} > ")
    url = f'https://freeipapi.com/api/json/{ip_address}'  
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        result = f"                                     {d}[{rs}IP Address{d}]{rs} {rs}{data.get('ipAddress', 'N/A')}\n" \
                 f"                                     {d}[{rs}Country{d}]{rs} {rs}{data.get('countryName', 'N/A')}\n" \
                 f"                                     {d}[{rs}Region{d}]{rs}  {rs}{data.get('regionName', 'N/A')}\n" \
                 f"                                     {d}[{rs}City{d}]{rs}  {rs}{data.get('cityName', 'N/A')}\n" \
                 f"                                     {d}[{rs}ISP{d}]{rs}  {rs}{data.get('isp', 'N/A')}\n" \
                 f"                                     {d}[{rs}Latitude{d}]{rs}  {rs}{data.get('latitude', 'N/A')}\n" \
                 f"                                     {d}[{rs}Longitude{d}]{rs}  {rs}{data.get('longitude', 'N/A')}\n"
        await clear()
        await logo()         
        print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} IP Lookup Results {g}[SUCCESS]{rs}")
        print(result)
    else:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to retrieve data: {response.text} {r}[FAILURE]{rs}")
