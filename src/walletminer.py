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

async def wallet_miner():
    await clear()
    await logo()
    wallet_address = input(f"                                     {d}[{rs}Wallet address{d}]{rs} > ")
    balance = 0.0  
    print(f"                                     {d}[{rs}Starting mining for wallet: {wallet_address}{d}]{rs} ")
    
    for i in range(5):
        time.sleep(2)  
        mined_amount = round(random.uniform(0.01, 0.5), 2) 
        balance += mined_amount
        print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Mined: {mined_amount} BTC | Total Balance: {balance} BTC {g}[SUCCESS]{rs}")
    print(f"                                     {d}[{rs}Mining complete for wallet: {wallet_address}{d}]{rs} ")
    print(f"                                     {d}[{rs}Final Balance: {balance} BTC{d}]{rs} ")
