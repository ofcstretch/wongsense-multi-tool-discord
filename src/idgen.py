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

async def id_gen():
    await clear()
    await logo()
    num_ids = int(input(f"                                     {d}[{rs}Amount of Id's{d}]{rs} > "))
    ids = []
    for _ in range(num_ids):
        name = fake.name()
        dob = fake.date_of_birth(minimum_age=18, maximum_age=90)  
        id_number = ''.join(random.choices(string.digits, k=9))
        state = fake.state_abbr()  
        issue_date = fake.date_between(start_date='-10y', end_date='today').strftime("%m/%d/%Y") 
        expiry_date = fake.date_between(start_date='today', end_date='+10y').strftime("%m/%d/%Y")  
        
        id = {
            "Name": name,
            "Date of Birth": dob.strftime("%m/%d/%Y"),
            "ID Number": id_number,
            "State": state,
            "Issue Date": issue_date,
            "Expiry Date": expiry_date,
        }
        
        ids.append(id)

    with open("ids.txt", 'w') as f:
        for id in ids:
            f.write(f"Name: {id['Name']}, DOB: {id['Date of Birth']}, ID Number: {id['ID Number']}, State: {id['State']}, Issue Date: {id['Issue Date']}, Expiry Date: {id['Expiry Date']}\n")

    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Generated {num_ids} IDs and saved to ids.txt {g}[SUCCESS]{rs}")