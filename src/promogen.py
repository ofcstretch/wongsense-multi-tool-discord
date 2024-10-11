import random
import string
import time
from style.clear import clear
from style.logo import logo

t = time.strftime('%H:%M:%S')

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def gen_promos():
    await clear()  
    await logo()   
    num_links = int(input(f"                                     {d}[{rs}Amount of promos{d}]{rs} > "))
    promo_links = []
    base_url = "https://discord.com/billing/promotions/"
    for _ in range(num_links):
        segments = []
        for _ in range(6):
            segment = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
            segments.append(segment)
        random_part = '-'.join(segments)
        promo_links.append(f"{base_url}{random_part}")
    with open("promos.txt", 'w') as f:
        for link in promo_links:
            f.write(f"{link}\n")
    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Generated {num_links} promotional links and saved to promo.txt {g}[SUCCESS]{rs}")
