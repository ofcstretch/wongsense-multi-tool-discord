import random
import string
import time
import asyncio
from style.logo import logo
from style.clear import clear

t = time.strftime('%H:%M:%S')
rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

async def gen_nitro():
    await clear()
    await logo()
    try:
        num_links = int(input(f"                                     {d}[{rs}{t}{d}]{rs} Enter the number of gift links to generate > "))
        if num_links <= 0:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Please enter a positive number {r}[FAILURE]{rs}")
            return
    except ValueError:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Invalid input. Please enter a number {r}[FAILURE]{rs}")
        return

    length = 16
    gift_links = []

    for _ in range(num_links):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        gift_link = f"https://discord.gift/{random_string}"
        gift_links.append(gift_link)

    with open("nitro.txt", "w") as file:
        for link in gift_links:
            file.write(link + "\n")           
    await clear()
    await logo()            
    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Generated {num_links} Discord gift links and saved to nitro.txt {g}[SUCCESS]{rs}")