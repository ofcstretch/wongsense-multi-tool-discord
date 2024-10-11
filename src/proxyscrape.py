import requests
import time
import asyncio
from style.logo import logo
from style.clear import clear
from bs4 import BeautifulSoup 

t = time.strftime('%H:%M:%S')
rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def proxy_scraper():
    await clear()
    await logo()
    
    print(f"                                     {d}[{rs}{t}{d}]{rs} Downloading proxies...")

    proxy_sources = [
        'https://www.proxy-list.download/api/v1/get?type=https',
        'https://www.sslproxies.org/',
        'https://www.free-proxy-list.net/anonymous-proxy.html',
        'https://www.us-proxy.org/',
        'https://www.proxynova.com/proxy-server-list/',
        'https://www.proxy-list.download/api/v1/get?type=socks5'
    ]

    proxies = set()  
    for source in proxy_sources:
        try:
            if 'sslproxies' in source or 'us-proxy' in source:
                response = requests.get(source)
                soup = BeautifulSoup(response.text, 'html.parser')
                for row in soup.find_all('tr'):
                    cols = row.find_all('td')
                    if len(cols) >= 2:
                        ip = cols[0].text.strip()
                        port = cols[1].text.strip()
                        proxies.add(f"{ip}:{port}")
            elif 'free-proxy-list' in source or 'proxynova' in source:
                response = requests.get(source)
                soup = BeautifulSoup(response.text, 'html.parser')
                for row in soup.find_all('tr'):
                    cols = row.find_all('td')
                    if len(cols) >= 2:
                        proxy = f"{cols[0].text.strip()}:{cols[1].text.strip()}"
                        proxies.add(proxy)
            else:
                response = requests.get(source)
                proxies.update(response.text.splitlines())
        except Exception as e:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Failed to download proxies from {source}: {str(e)} {r}[FAILURE]{rs}")
    if proxies:
        with open("utils/proxies.txt", "w") as file:
            for proxy in proxies:
                file.write(proxy + "\n")
        print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Downloaded {len(proxies)} proxies {g}[SUCCESS]{rs}")
    else:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} No proxies were found. {r}[FAILURE]{rs}")
    await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(proxy_scraper())