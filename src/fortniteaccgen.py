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

pro1 = ["Sweaty", "Pro", "Godly", "Elite", "Ninja", "Beast", "Savage", "Fury", "Stealth", "Blitz"]
pro2 = ["Sniper", "Warrior", "Builder", "Assassin", "Hunter", "Legend", "Master", "Champion", "Gamer", "Hero"]

async def fortnite_acc_gen():
    await clear()
    await logo()
    num_accounts = int(input(f"                                     {d}[{rs}Amount of Fn Accs{d}]{rs} > "))
    accounts = []
    for _ in range(num_accounts):
        username = f"{random.choice(pro1)}{random.choice(pro2)}{random.randint(100, 999)}"  
        email = fake.email() 
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))  
        account_info = {
            "Username": username,
            "Email": email,
            "Password": password
        }
        
        accounts.append(account_info)
    with open("fortnite_accounts.txt", 'w') as f:
        for account in accounts:
            f.write(f"Username: {account['Username']}, Email: {account['Email']}, Password: {account['Password']}\n")

    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Generated {num_accounts} Fortnite accounts and saved to fortnite_accounts.txt {g}[SUCCESS]{rs}")