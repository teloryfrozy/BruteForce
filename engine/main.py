from colorama import Fore
from password_list_generator import run_generator


#################################################
###               USER INTERFACE              ###
#################################################

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
    print(f"{Fore.YELLOW}?d : {Fore.RESET}0123456789")
    print(f"{Fore.YELLOW}?l : {Fore.RESET}abcdefghijklmnopqrstuvwxyz")
    print(f"{Fore.YELLOW}?L : {Fore.RESET}ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(f"{Fore.YELLOW}?e : {Fore.RESET}àéè€ù£ç")
    print(f"{Fore.YELLOW}?s : " + Fore.RESET + "!@#$%^&*()-_+={}[]|\\:;\"',./<>?~`space")
    print(f"{Fore.YELLOW}?a : {Fore.RESET}?dlLse")
    print()
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
        for letter in element:
            if letter not in "adlLse":
                wrong_format()
                return False
            
    return list_letters
    

if __name__ == "__main__":
    info_msg()

    list_letters = ask_format()
    while list_letters == False:
        list_letters = ask_format()

    print(f"{Fore.GREEN}Thank you for providing us with the format of the password{Fore.RESET}")
    
    # --- Output file --- #
    print()
    print("---------------------------------------------------------")
    filename = input("Enter the name of the output file: ")
    run_generator(filename, list_letters)