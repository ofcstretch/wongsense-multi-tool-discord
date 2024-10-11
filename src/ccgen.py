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

async def cc_gen():
    await clear()
    await logo()
    num_cards = int(input(f"                                     {d}[{rs}Amount of Cc{d}]{rs} > "))
    def luhn_check(card_number):
        total = 0
        reverse_digits = [int(d) for d in str(card_number)][::-1]
        for i, digit in enumerate(reverse_digits):
            if i % 2 == 1:  
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit
        return total % 10 == 0
    fake_cc_list = []
    card_providers = {
        "Visa": "4",
        "MasterCard": "5",
        "American Express": "34",
        "Discover": "6",
    }
    for _ in range(num_cards):
        provider = random.choice(list(card_providers.keys()))
        prefix = card_providers[provider]
        if provider == "American Express":
            card_number = prefix + ''.join(random.choices('0123456789', k=13)) 
        else:
            card_number = prefix + ''.join(random.choices('0123456789', k=15))  
        if not luhn_check(card_number):
            card_number = str(random.randint(4000, 4999)) + ''.join(random.choices('0123456789', k=15))
        expiration_date = f"{random.randint(1, 12):02}/{random.randint(23, 30)}"  
        cvv = ''.join(random.choices('0123456789', k=3)) 
        fake_cc_list.append(f"Card Number: {card_number}, Expiration Date: {expiration_date}, CVV: {cvv}")
    with open("cc.txt", 'w') as f:
        for cc in fake_cc_list:
            f.write(f"{cc}\n")
    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Generated {num_cards} credit cards and saved to cc.txt {g}[SUCCESS]{rs}")
