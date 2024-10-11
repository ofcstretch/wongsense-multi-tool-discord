import random
import string
import time
from faker import Faker
from style.clear import clear
from style.logo import logo

t = time.strftime('%H:%M:%S')

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

fake = Faker()

async def discord_acc_gen():
    await clear()
    await logo()
    num_accounts = int(input(f"                                     {d}[{rs}Amount of Accs{d}]{rs} > "))
    accounts = []
    for _ in range(num_accounts):
        username = fake.user_name() 
        email = fake.email()          
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12)) 
        accounts.append({
            "Username": username,
            "Email": email,
            "Password": password
        })
        print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Generated account: {username} | {email} | Password: {password} {g}[SUCCESS]{rs}")
    with open("discord_accounts.txt", 'w') as f:
        for acc in accounts:
            f.write(f"Username: {acc['Username']}, Email: {acc['Email']}, Password: {acc['Password']}\n")
    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Generated {num_accounts} Discord accounts and saved to discord_accounts.txt {g}[SUCCESS]{rs}")
