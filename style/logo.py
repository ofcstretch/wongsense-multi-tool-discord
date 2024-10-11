from pystyle import *

async def logo():
    logo = """                                        
                                     _ _ _ _____ _____ _____ _____ _____ _____ _____ _____ 
                                    | | | |     |   | |   __|   __|   __|   | |   __|   __|
                                    | | | |  |  | | | |  |  |__   |   __| | | |__   |   __|
                                    |_____|_____|_|___|_____|_____|_____|_|___|_____|_____|
    """
    logo_color = Colorate.Horizontal(Colors.cyan_to_blue, logo)
    print(logo_color)