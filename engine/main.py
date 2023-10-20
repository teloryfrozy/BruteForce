#!/usr/bin/env python
# -*- coding:utf-8 -*-

# TODO
# handle the fact that the user may now that the password start by a certain string
# and finish by a list of numbers between 2 and 4
# examples:
# pAssWord123
# pAssWord12

'''
 ============================================================================
 Name        : password_list_generator.py
 Author      : Augustin ROLET
 Version     : 1.0
 Copyright   : Copyright Free
 Description : Password list generator inspired by Kali Linux
 ============================================================================
'''

from password_list_generator import run_generator


def ask_feature():
    """Displays all the available features"""
    print("What you can do with this tool?")
    print("... Generate a passwords list")
    print("... Run an attack to a WiFi network")
    print("... Find the password of an encrypted file")
    print("... Find the password of a KeePassXC database")

def info_msg():
    """Displays a banner"""
    print("=========================================================")
    print("Password list generator")
    print()
    print("Character formats available:")
    print("?d : 0123456789")
    print("?l : abcdefghijklmnopqrstuvwxyz")
    print("?L : ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print("?e : àéè€ù£ç")
    print("?s : !@#$%^&*()-_+={}[]|\\:;\"',./<>?~`space")
    print("?a : ?dlLse")
    print("Examples of usage:")
    print("- ?d?e?L?l")
    print("- ?d?d?d?d?d?d?d")
    print("- ?d+knowPart1?d+knownPart2")
    print("=========================================================")

def wrong_format():
    """Displays an error message and recall the format"""
    print("\n\n")
    print("Input format is not valid")
    print("Examples of usage:")
    print("- ?d?e?L?l")
    print("- ?d?d?d?d?d?d?d")

def ask_format():
    print("\n\n")
    pwd_format = input("Enter the format of the password: ").strip()
    
    # --- DEBUGGING --- #
    if pwd_format[-1] == "?":
        wrong_format()
        return False
    # list of the letters
    list_letters = pwd_format.split("?")
    list_letters.pop(0)

    if not (len(list_letters) <= 32):
        wrong_format()
        return False
    for element in list_letters:
        # TODO: check if the user entered a format like that ?aaaaaaaaaaa?eeeee?d?d
        for letter in element:
            if letter not in "adlLse":
                wrong_format()
                return False
            
    return list_letters
    

info_msg()

list_letters = ask_format()
while list_letters == False:
    list_letters = ask_format()


print("\033[92mThank you for providing us with the format of the password\033[0m")
print("\033[0m") # reset the color
print("---------------------------------------------------------")
print("Range of characters")
print("Minimum: 1, Maximum: 32")
print("Pay attention, a range is only available for these cases:")
print("- If all the characters are ?a")
print("- If all the characters are of the same type")


# --- Output file --- #
print()
print("---------------------------------------------------------")
filename = input("Enter the name of the output file: ")
print(f"This is list_letters = {list_letters}")
run_generator(filename, list_letters)


# TODO: run test on a powerful computer
# Generate the passwords list according to this patterns
# ?L?l?l?l?s?d?d?d?d
# ?l?d?l?d?d?d?d?d
