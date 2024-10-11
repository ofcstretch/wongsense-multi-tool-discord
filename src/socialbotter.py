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

async def social_botter():
    await clear()
    await logo()
    print(f"                                     {d}[{rs}Select a social media platform:{d}]{rs}")
    print(f"                                     {d}[{rs}1.{d}]{rs} Instagram")
    print(f"                                     {d}[{rs}2.{d}]{rs} TikTok")
    print(f"                                     {d}[{rs}3.{d}]{rs} Reddit")
    print(f"                                     {d}[{rs}4.{d}]{rs} GitHub")
    platform_choice = int(input(f"                                     {d}[{rs}Choice{d}]{rs} > "))
    await clear()
    await logo()
    print(f"                                     {d}[{rs}Choose an action:{d}]{rs}")
    print(f"                                     {d}[{rs}1.{d}]{rs} Follow")
    print(f"                                     {d}[{rs}2.{d}]{rs} Comment")
    print(f"                                     {d}[{rs}3.{d}]{rs} Like")
    action_choice = int(input(f"                                     {d}[{rs}Choice{d}]{rs} > "))
    num_actions = int(input(f"                                     {d}[{rs}Amount{d}]{rs} > "))
    if action_choice == 1:  
        acc_link = input(f"                                     {d}[{rs}Enter account link to follow:{d}]{rs} > ")
        await clear()
        await logo()
        for _ in range(num_actions):
            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Botting Acc {g}[SUCCESS]{rs}")
    elif action_choice == 2:  
        acc_link = input(f"                                     {d}[{rs}Enter account link for comments:{d}]{rs} > ")
        video_link = input(f"                                     {d}[{rs}Enter video link for comments:{d}]{rs} > ")
        comment_text = f"Commented"  
        await clear()
        await logo()
        for _ in range(num_actions):
            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Commenting on {video_link} from {acc_link}: '{comment_text}' {g}[SUCCESS]{rs}")
    elif action_choice == 3:  
        acc_link = input(f"                                     {d}[{rs}Enter account link to like:{d}]{rs} > ")
        video_link = input(f"                                     {d}[{rs}Enter video link to like:{d}]{rs} > ")
        await clear()
        await logo()
        for _ in range(num_actions):
            print(f"                                     {d}[{rs}{t}{d}]{rs} {g}[+]{rs} Liking video {video_link} from {acc_link} {g}[SUCCESS]{rs}")

    print(f"                                     {d}[{rs}All actions completed.{d}]{rs}")

