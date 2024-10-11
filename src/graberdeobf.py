import requests
import time
from tkinter import Tk, filedialog
from style.clear import clear
from style.logo import logo
import json

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
t = time.strftime('%H:%M:%S')

async def grabber_deobf():
    await clear()
    await logo()
    root = Tk()
    root.withdraw()  
    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Please select a file > ")
    file_path = filedialog.askopenfilename()
    if not file_path:
        print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} No file selected {r}[FAILURE]{rs}")
        return
    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Selected file > {file_path}")
    url = 'https://lululepu.fr/ungrabber'
    files = {'file': open(file_path, 'rb')}

    try:
        response = requests.post(url, files=files)

        if response.status_code == 200:
            try:
                data = response.json()
                if 'result' in data:
                    webhook = data['result']  
                    print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Webhook found > {webhook} {g}[SUCCESS]{rs}")
                else:
                    print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} No key found in response {r}[FAILURE]{rs}")
            except json.JSONDecodeError:
                print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Response is not valid JSON {r}[FAILURE]{rs}")
        else:
            print(f"                                     {d}[{rs}{t}{d}]{rs} {r}[-]{rs} Error uploading file: {response.status_code} {r}[FAILURE]{rs}")
    finally:
        files['file'].close()  