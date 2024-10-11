import time
import asyncio
import os
import sys
import platform
import hashlib
from pystyle import *
from auth.keyauth import api
from src.tokeninfo import info  
from src.guildchecker import get_guilds  
from src.leaveallservers import leave_all_servers
from src.massdm import massdm
from src.massgc import massgc
from src.tokenformatter import tokenformatter
from src.statuschanger import change_status
from src.hypesquadchanger import change_hypesquad
from src.tokenchecker import token_checker
from src.seizure import seizure
from src.channelspammer import channel_spammer
from src.threadspammer import thread_spammer
from src.closealldms import close_all_dms
from src.blockall import block_everyone
from src.changelanguage import change_language
from src.tokenfucker import destroy
from src.serverinfo import server_info
from src.nitrogen import gen_nitro
from src.massreact import mass_react
from src.faketyping import fake_typing
from src.serverdisplaychanger import serverdisplaychanger
from src.graberdeobf import grabber_deobf
from src.emailbomber import bomb
from src.proxyscrape import proxy_scraper
from src.proxychecker import proxy_checker
from src.promogen import gen_promos
from src.gmailgen import gen_gmails
from src.ccgen import cc_gen
from src.idgen import id_gen
from src.walletminer import wallet_miner
from src.socialbotter import social_botter
from src.accgen import discord_acc_gen
from src.fortniteaccgen import fortnite_acc_gen
from src.tokenlogin import token_login
from src.iplookup import ip_lookup
from src.messagedeleter import delete_messages
from src.terminator import terminate
from src.webhookspammer import webhook_spammer
from style.tokencount import tkn


async def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

rs = "\033[31m" 
d = '\033[38;2;50;100;255m'  
r = "\033[0m" 
c = "\033[36m"  
g = "\033[32m"
t = time.strftime('%H:%M:%S')


async def logo():
    token_count = tkn()
    logo = f"""                                        
                                     _ _ _ _____ _____ _____ _____ _____ _____ _____ _____ 
                                    | | | |     |   | |   __|   __|   __|   | |   __|   __| ({token_count}) = Tokens
                                    | | | |  |  | | | |  |  |__   |   __| | | |__   |   __|  Version = Premium    
                                    |_____|_____|_|___|_____|_____|_____|_|___|_____|_____|   Made by = ipesp, pystyle, _h3          
    """
    logo_color = Colorate.Horizontal(Colors.cyan_to_blue, logo)
    print(logo_color)

async def menu(tokens):
    while True:
        await clear()
        await logo()
        token_count = tkn()
        menu_options = f"""{rs}
                                        {d}[{r}01{d}]{r} Token Info            {d}[{r}06{d}]{r} Status Changer
                                        {d}[{r}02{d}]{r} Token Guild Check     {d}[{r}07{d}]{r} Hypesquad Changer
                                        {d}[{r}03{d}]{r} Token Formatter       {d}[{r}08{d}]{r} Mass GC
                                        {d}[{r}04{d}]{r} Token Checker         {d}[{r}09{d}]{r} Mass DM
                                        {d}[{r}05{d}]{r} Token Leaver          {d}[{r}10{d}]{r} Next Page
    """
        print(menu_options)

        choice = await asyncio.get_event_loop().run_in_executor(None, input, f"                                        {d}[{r}Wongsense{d}]{r} {d}>{r} ")

        if choice == "1":
            await info()  
        elif choice == "2":
            await get_guilds()  
        elif choice == "3":
                await tokenformatter()   
        elif choice == "4":
            await token_checker() 
        elif choice == "5":
            await leave_all_servers()  
        elif choice == "6":
            await change_status()
        elif choice == "7":
            await change_hypesquad()   
        elif choice == "8":
            await massgc()  
        elif choice == "9":
            await massdm()  
        elif choice == "10":
            await menu2(tokens)                                                
        else:
            print(f"                                        {d}[{r}Wongsense{d}]{r} Invalid Option")
            await asyncio.sleep(2) 

        await asyncio.get_event_loop().run_in_executor(None, input, f"                                     {d}[{r}Wongsense{d}]{r} > Press Enter to return")

async def menu2(tokens):
    while True:
        await clear()
        await logo()
        menu_options = f"""
                                        {d}[{r}11{d}]{r} Guild Information       {d}[{r}16{d}]{r} Nitro Generator
                                        {d}[{r}12{d}]{r} Token Nuker             {d}[{r}17{d}]{r} Proxy Scraper 
                                        {d}[{r}13{d}]{r} Language Changer        {d}[{r}18{d}]{r} Proxy Checker
                                        {d}[{r}14{d}]{r} Grabber Deobfuscator    {d}[{r}19{d}]{r} Previous Page
                                        {d}[{r}15{d}]{r} Email Bomber            {d}[{r}20{d}]{r} Next Page    
    """
        print(menu_options)

        choice = await asyncio.get_event_loop().run_in_executor(None, input, f"                                        {d}[{r}Wongsense{d}]{r} {d}>{r} ")
        if choice == "11":
            await server_info()
        elif choice == "12":
            await destroy()
        elif choice == "13":
            await change_language()  
        elif choice == "14":
            await grabber_deobf()
        elif choice == "15":
            await bomb()
        elif choice == "16":
            await gen_nitro()
        elif choice == "17":
            await proxy_scraper()
        elif choice == "18":
            await proxy_checker()
        elif choice == "19":
            await menu(tokens)
        elif choice == "20":
            await menu3(tokens)    
        else:
            print(f"                                        {d}[{r}Wongsense{d}]{r} Invalid option")
            await asyncio.sleep(2)
        await asyncio.get_event_loop().run_in_executor(None, input, f"                                     {d}[{r}Wongsense{d}]{r} > Press Enter to return")

async def menu3(tokens):
    while True:
        await clear()
        await logo()
        menu_options = f"""
                                        {d}[{r}21{d}]{r} Channel Spammer   {d}[{r}26{d}]{r} React
                                        {d}[{r}22{d}]{r} Thread Spammer    {d}[{r}27{d}]{r} Fake Typing
                                        {d}[{r}23{d}]{r} Token Login       {d}[{r}28{d}]{r} Server Name Changer
                                        {d}[{r}24{d}]{r} Close All DMS     {d}[{r}29{d}]{r} Previous Page
                                        {d}[{r}25{d}]{r} Block Everyone    {d}[{r}30{d}]{r} Next Page
        """
        print(menu_options)

        choice = await asyncio.get_event_loop().run_in_executor(None, input, f"                                        {d}[{r}Wongsense{d}]{r} {d}>{r} ")                                        

        if choice == "21":
            await channel_spammer()
        elif choice == "22":
            await thread_spammer()   
        elif choice == "23":
            await token_login()
        elif choice == "24":
            await close_all_dms()  
        elif choice == "25":
            await block_everyone()
        elif choice == "26":
            await mass_react()   
        elif choice == "27":
            await fake_typing()   
        elif choice == "28":
            await serverdisplaychanger()                                      
        elif choice == "29":
            await menu2(tokens)   
        elif choice == "30":
            await menu4(tokens)         
        else:
            print(f"                                        {d}[{r}Wongsense{d}]{r} Invalid Option")
            await asyncio.sleep(2) 

        await asyncio.get_event_loop().run_in_executor(None, input, f"                                        {d}[{r}Wongsense{d}]{r} > Press Enter to return")


async def menu4(tokens):
    while True:
        await clear()
        await logo()
        menu_options = f"""
                                        {d}[{r}31{d}]{r} Seizure          {d}[{r}36{d}]{r} Troll Page
                                        {d}[{r}32{d}]{r} webhook spammer  {d}[{r}37{d}]{r} Previous Page
                                        {d}[{r}33{d}]{r} Message Deleter 
                                        {d}[{r}34{d}]{r} Ip Lookup   
                                        {d}[{r}35{d}]{r} Terminator     
        """
        print(menu_options)

        choice = await asyncio.get_event_loop().run_in_executor(None, input, f"                                        {d}[{r}Wongsense{d}]{r} {d}>{r} ") 

        if choice == "31":
            await seizure()
        if choice == "32":
            await webhook_spammer()        
        elif choice == "33":
            await delete_messages()    
        elif choice == "34":
            await ip_lookup() 
        elif choice == "35":
            await terminate()            
        elif choice == "36":
            await troll_menu(tokens)
        elif choice == "37":
            await menu3(tokens)            
        else:
            print(f"                                        {d}[{r}Wongsense{d}]{r} Invalid Option")
            await asyncio.sleep(2) 

        await asyncio.get_event_loop().run_in_executor(None, input, f"                                     {d}[{r}Wongsense{d}]{r} > Press Enter to return")

async def troll_menu(tokens):
    while True:
        await clear()
        await logo()
        menu_options = f"""
                                        {d}[{r}38{d}]{r} Promo Gen          {d}[{r}43{d}]{r} Social Botter
                                        {d}[{r}39{d}]{r} Gmail Gen          {d}[{r}44{d}]{r} Discord Acc Gen
                                        {d}[{r}40{d}]{r} Identity Gen       {d}[{r}45{d}]{r} Fortnite Acc Gen
                                        {d}[{r}41{d}]{r} CC Gen             {d}[{r}46{d}]{r} Previous Page
                                        {d}[{r}42{d}]{r} Wallet Miner       
        """
        print(menu_options)

        choice = await asyncio.get_event_loop().run_in_executor(None, input, f"                                        {d}[{r}Wongsense{d}]{r} {d}>{r} ") 

        if choice == "38":
            await gen_promos()
        elif choice == "39":
            await gen_gmails()   
        elif choice == "40":
            await id_gen()    
        elif choice == "41":
            await cc_gen()     
        elif choice == "42":
            await wallet_miner() 
        elif choice == "43":
            await social_botter() 
        elif choice == "44":
            await discord_acc_gen()  
        elif choice == "45":
            await fortnite_acc_gen()        
        elif choice == "46":
            await menu4(tokens)    
        else:
            print(f"                                        {d}[{r}Wongsense{d}]{r} Invalid Option")
            await asyncio.sleep(2) 

        await asyncio.get_event_loop().run_in_executor(None, input, f"                                     {d}[{r}Wongsense{d}]{r} > Press Enter to return")


if __name__ == "__main__":
    with open('utils/tokens.txt') as f:
        tokens = f.read().splitlines()
    asyncio.run(menu())