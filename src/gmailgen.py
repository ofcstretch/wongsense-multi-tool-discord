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

async def gen_gmails():
    await clear()  
    await logo()   
    domain = input(f"                                     {d}[{rs}Gmail Domain{d}]{rs} > ")
    num_emails = int(input(f"                                     {d}[{rs}Amount of gmails{d}]{rs} > "))
    email_addresses = []
    for _ in range(num_emails):
        username_length = random.randint(8, 12)
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=username_length))
        email_addresses.append(f"{username}{domain}")
    with open("emails.txt", 'w') as f:
        for email in email_addresses:
            f.write(f"{email}\n")
    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Generated {num_emails} email addresses and saved to emails.txt {g}[SUCCESS]{rs}")
