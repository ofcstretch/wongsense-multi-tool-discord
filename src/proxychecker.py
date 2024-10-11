import aiohttp
import asyncio
import time
from style.clear import clear
from style.logo import logo

t = time.strftime('%H:%M:%S')
rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def check_proxy(session, proxy):
    if proxy.startswith("socks5://"):
        proxy_type = "socks5"
        proxy_url = proxy
    elif proxy.startswith("socks4://"):
        proxy_type = "socks4"
        proxy_url = proxy
    elif proxy.startswith("http://"):
        proxy_type = "http"
        proxy_url = proxy
    elif proxy.startswith("https://"):
        proxy_type = "https"
        proxy_url = proxy
    else:
        proxy_url = f"http://{proxy}" 
    try:
        async with session.get('https://httpbin.org/ip', proxy=proxy_url, timeout=3) as response:
            if response.status == 200:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Proxy: {proxy} is valid {g}[SUCCESS]{rs}")
                return True
            else:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Proxy: {proxy} is invalid {r}[FAILURE]{rs}")
                return False
    except Exception:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Proxy: {proxy} is invalid {r}[FAILURE]{rs}")
        return False

async def proxy_checker():
    await clear()
    await logo()
    
    with open('utils/proxies.txt', 'r') as file:
        proxies = [proxy.strip() for proxy in file.readlines() if proxy.strip()]

    valid_count = 0
    invalid_count = 0

    async with aiohttp.ClientSession() as session:
        tasks = [check_proxy(session, proxy) for proxy in proxies]
        results = await asyncio.gather(*tasks)
    
    valid_count = sum(results)
    invalid_count = len(results) - valid_count

    print(f"                                     {d}[{rs}{t}{d}]{rs} {d}[{rs}RESULTS{d}]{rs} > ")
    print(f"                                     {d}[{rs}{t}{d}]{rs} {d}[{rs}Valid Proxies{d}]{rs}   : {valid_count} {g}[SUCCESS]{rs}")
    print(f"                                     {d}[{rs}{t}{d}]{rs} {d}[{rs}Invalid Proxies{d}]{rs} : {invalid_count} {r}[FAILURE]{rs}")

if __name__ == "__main__":
    asyncio.run(proxy_checker())