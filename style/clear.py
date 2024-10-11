import os

async def clear():
    os.system('cls' if os.name == 'nt' else 'clear')