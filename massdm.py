import requests
import time
import random
from colorama import Fore
import json
import colorama

with open("config.json") as conf:
    config = json.load(conf)
    token = config["token"]

rs = requests.Session()

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def mass_dm():
    colorama.init()
    message = input('Message: ')
    headers = {"authorization": token, "user-agent": "Mozilla/5.0"}

    reqmas = rs.get(
        "https://discord.com/api/v9/users/@me/channels", headers=headers
    ).json()
    for chen in reqmas:
        json = {"content": message}
        time.sleep(1)
        rs.post(
            f"https://discord.com/api/v9/channels/{chen['id']}/messages",
            headers=headers,
            data=json,
        )
        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} {chen['id']} Sent")

mass_dm()