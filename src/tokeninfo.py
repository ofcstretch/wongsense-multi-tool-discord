import httpx
from datetime import datetime
import asyncio
import time
import aiofiles
from style.logo import logo
from style.clear import clear

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"
y = "\033[0;33m"

languages = {
    'da': 'Danish, Denmark',
    'de': 'German, Germany',
    'en-GB': 'English, United Kingdom',
    'en-US': 'English, United States',
    'es-ES': 'Spanish, Spain',
    'fr': 'French, France',
    'hr': 'Croatian, Croatia',
    'lt': 'Lithuanian, Lithuania',
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukrainian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

async def info():
    await clear()
    await logo()
    async with aiofiles.open('utils/tokens.txt', 'r') as file:
        tokens = [line.strip() for line in await file.readlines() if line.strip()]

    if not tokens:
        print(f"                                     {d}[{rs}Error{d}]{rs} No tokens found in the file! {r}[FAILURE]{rs}")
        return

    choice = input(f"                                     {d}[{rs}Wongsense{d}]{rs} > Enter t for txt or w for webhook > ").lower()
    
    webhook_url = None
    if choice == 'w':
        await clear()
        await logo()
        webhook_url = input(f"                                     {d}[{rs}Wongsense{d}]{rs} > Enter Webhook URL: ")

    async with httpx.AsyncClient() as client:
        for token in tokens:
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json'
            }

            res = await client.get('https://discord.com/api/v9/users/@me', headers=headers)
            t = time.strftime('%H:%M:%S')

            if res.status_code == 200:
                res_json = res.json()
                user_name = f'{res_json["username"]}'
                user_id = res_json['id']
                avatar_id = res_json['avatar']
                avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
                phone_number = res_json.get('phone', 'Not Provided')
                email = res_json.get('email', 'Not Provided')
                mfa_enabled = res_json['mfa_enabled']
                flags = res_json['flags']
                locale = res_json['locale']
                verified = res_json['verified']
                language = languages.get(locale, "Not specified")
                creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')

                nitro_data = await client.get('https://discord.com/api/v9/users/@me/billing/subscriptions', headers=headers)
                has_nitro = False
                nitro_days_left = None

                if nitro_data.status_code == 200:
                    nitro_data_json = nitro_data.json()
                    has_nitro = bool(len(nitro_data_json) > 0)
                    if has_nitro:
                        end_date = datetime.strptime(nitro_data_json[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                        nitro_days_left = (end_date - datetime.now()).days

                info_text = f"""
Username: {user_name}
User ID: {user_id}
Avatar URL: {avatar_url}
Creation Date: {creation_date}
Phone Number: {phone_number}
Email: {email}
2FA/MFA Status: {'Enabled' if mfa_enabled else 'Disabled'}
Account Flags: {flags}
Locale: {locale} ({language})
Email Status: {'Verified' if verified else 'Not Verified'}
Nitro: {'Has Nitro with ' + str(nitro_days_left) + ' days left' if has_nitro else 'No Nitro'}
"""

                if choice == 't':
                    await clear()
                    await logo()
                    with open(f'{user_name}_info.txt', 'w') as f:
                        f.write(info_text)
                    print(f"                                     {d}[{rs}{t}{d}]{rs} Info saved to {user_name}_info.txt {g}[SUCCESS]{rs}")
                elif choice == 'w' and webhook_url:
                    data = {
                        "content": f"```{info_text}```",
                        "username": "Wongsense"
                    }
                    webhook_res = await client.post(webhook_url, json=data)
                    if webhook_res.status_code == 204:
                        print(f"                                     {d}[{rs}{t}{d}]{rs} Info sent to webhook successfully {g}[SUCCESS]{rs}")
                    else:
                        print(f"                                     {d}[{rs}{t}{d}]{rs} Error sending to webhook: {webhook_res.status_code} {r}[FAILURE]{rs}")
            else:
                print(f"                                     {d}[{rs}{t}{d}]{rs} Error fetching token information: {res.status_code} - {res.text} {r}[FAILURE]{rs}")