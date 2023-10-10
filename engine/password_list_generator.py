'''
 ============================================================================
 Name        : password_list_generator.py
 Author      : Augustin ROLET
 Version     : 1.0
 Copyright   : Copyright Free
 Description : Password list generator inspired by Kali Linux
 ============================================================================
'''

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
    print("?s : !@#$%^&*()-_+={}[]|\\:;\"',./<>?~` space")
    print("?a : ?dlLse")
    print("Examples of usage:")
    print("- ?d?e?L?l")
    print("- ?d?d?d?d?d?d?d")
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
    print("Enter the format of the password")
    pwd_format = input("").strip()
    
    # --- DEBUGGING --- #
    if pwd_format[-1] == "?":
        wrong_format()
        return False
    # list of the letters
    list_letters = pwd_format.split("?")
    list_letters.pop(0)

    if not (4 <= len(list_letters) <= 32):
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
 
print("Thank to provide us the format of the password")
print()
print("---------------------------------------------------------")
print("Range of characters")
print("Minimum: 4, Maximum: 32")
print("Pay attention, a range is only available for these cases:")
print("- If all the characters are ?a")
print("- If all the characters are of the same type")

# TODO
# handle the fact that the user may now that the password start by a certain string
# and finish by a list of numbers between 2 and 4
# examples:
# pAssWord123
# pAssWord12