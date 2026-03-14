import sys
import time
import re
import pyshorteners
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

VERSION = "1.0"

telegram = "https://t.me/monkrk"
github = "https://github.com/mrdigitalmonk"

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
Y = '\033[33m'
W = '\033[0m'

banner = r'''
   ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓ ███▄ ▄███▓ ▄▄▄        ██████  ██ ▄█▀
  ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▓██▒▀█▀ ██▒▒████▄    ▒██    ▒  ██▄█▒ 
 ▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▓███▄░ 
 ░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ ▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒▓██ █▄ 
 ░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒▒██▒ █▄
  ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒
   ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒ ▒░
 ░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      ░      ░     ░   ▒   ░  ░  ░  ░ ░░ ░ 
       ░  ░  ░  ░    ░ ░        ░                  ░         ░  ░      ░  ░  ░   

             👻  GhostMask by Digital Monk. ⚔️
                 ☢️ End is the Beginning ☢️
'''

def show_banner():
    print(f"{C}{banner}{W}")
    print(f"{G}Version : {W}{VERSION}")
    print(f"{G}Telegram: {W}{telegram}")
    print(f"{G}GitHub  : {W}{github}")
    print()

def loading():
    frames = ["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"]
    for _ in range(6):
        for f in frames:
            sys.stdout.write(f"\r{C}Generating masked links {f}{W}")
            sys.stdout.flush()
            time.sleep(0.1)
    print()

def tool_info():

    print(f"""{C}

👻 GhostMask Info ⚔️
-------------------------
Tool       : URL Masking Tool
Version    : {VERSION}
Creator    : Digital Monk

Platforms  : Kali Linux / Termux

Description:
GhostMask masks URLs using
multiple shorteners to create
clean redirect links.

Telegram   : {telegram}
GitHub     : {github}

Tagline    : End is the Beginning
-------------------------
{W}""")

def mask_url(domain, keyword, url):
    parsed = urlparse(url)
    return f"{parsed.scheme}://{domain}-{keyword}@{parsed.netloc}{parsed.path}"

def generate():

    while True:
        web_url = input(f"{G}Enter original URL {W}(ex: https://example.com): ")
        if re.match(r'^(https?://)', web_url):
            break
        print(f"{R}Invalid URL format{W}")

    while True:
        domain = input(f"{Y}Enter custom domain {W}(ex: gmail.com): ")
        if "." in domain:
            break
        print(f"{R}Invalid domain{W}")

    while True:
        keyword = input(f"{Y}Enter masking keyword {W}(ex: login): ")
        if " " not in keyword and len(keyword) <= 15:
            break
        print(f"{R}Invalid keyword{W}")

    loading()

    s = pyshorteners.Shortener()

    shorteners = [
        s.tinyurl,
        s.dagd,
        s.clckru,
        s.osdb
    ]

    def shorten(service):
        try:
            return service.short(web_url)
        except:
            return None

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(shorten, shorteners))

    short_urls = [r for r in results if r]

    print(f"\n{R}Original URL:{W} {web_url}\n")
    print(f"{G}Generated Masked URLs:{W}")

    for i, url in enumerate(short_urls):
        masked = mask_url(domain, keyword, url)
        print(f"{C}[{i+1}]{W} {masked}")

def menu():

    while True:

        print(f"""
{Y}------------------------------
        👻 GhostMask
------------------------------
[1] Generate Masked URL
[2] Tool Info
[3] Exit
------------------------------{W}
""")

        choice = input("Select option > ")

        if choice == "1":
            generate()

        elif choice == "2":
            tool_info()

        elif choice == "3":
            print("Exiting GhostMask...")
            sys.exit()

        else:
            print("Invalid option")

show_banner()
menu()