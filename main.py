from colorama import Fore
import requests
import random
import threading
import time
import string
import os, json

from nickname_generator import generate
M = Fore.LIGHTMAGENTA_EX
W = Fore.RESET
G = Fore.GREEN
R = Fore.RED
from datetime import datetime

def main():
    os.system("cls")
    os.system("title GuildedGen V5")
    #print(f"{M}Guilded Gen V5{W} | Dev: {M}vilinta")
    #print(f"{W}[{M}1{W}] Random gmail | {W}[{M}2{W}] Gmail plus trick | {W}[{M}3{W}] Custom email list\n")

with open("proxies.txt", "r") as f:
    proxies = f.read().splitlines()
f.close()

main()
with open('config.json') as r:
    config = json.load(r)

FabiArbeit123 = config.get('invitestobypasscooldown')
niggers = config.get('invitecode')
choice = ("1")

def balls():
    FabiArbeit = FabiArbeit123
    return random.choice(FabiArbeit)
def randstr(length):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return "".join(random.sample(chars, length))

def gen():
    global generated
    proxy = random.choice(proxies)
    session = requests.Session()
    base_url = "https://www.guilded.gg/api"
    session.proxies = {"https": f"http://{proxy}", "http": f"https://{proxy}"}
    while True:

        email = f"{generate('en')}_{generate('en')}@guilded.gen"
        password = f"GuildedGen{randstr(24)}"
        username = f"{randstr(23)}"
        payload = {"email": email, "password": password, "name": username, "fullName": username}
        try:
            r = session.post("https://www.guilded.gg/api/users?type=email", json=payload)
            cookie = r.cookies["hmac_signed_session"]
            session.headers = {"cookie": f"hmac_signed_session={cookie}"}
            r = session.put(f"https://www.guilded.gg/api/invites/{invite}")
            session.put("%s/users/me/ping" % (base_url), json={})
            #ss = session.post("%s/users/me/friendrequests" % (base_url), json={ friend
            #"friendUserIds": 'mbEW0N6d'
            #})
            session.post("%s/users/me/profile/images" % (base_url), json={
            "imageUrl": "none"
            })
            now = datetime.now().strftime("%H:%M:%S")
            print(f"[{now}] | {cookie[:73]}")
            generated += 1
            os.system(f"title GuildedGen V5 Generated: {generated}")
            af = open(f"{invite}.txt", "a")
            af.write(f"{email}:{password}:{cookie}\n")
            af.close()
            af = open("cookies.txt", "a")
            af.write(f"{cookie}\n")
            af.close()
        except:
            pass


if choice == "1":
    generated = 0
    invite = (balls())
    #emaillength = input(f"{W}Emails length: {M}")
    os.system("cls")
    for x in range(1500):
        threading.Thread(target=gen).start()
