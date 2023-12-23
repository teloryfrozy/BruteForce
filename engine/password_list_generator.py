from os import listdir
from tqdm import tqdm
from colorama import Fore


##########################################
# --- DEFINITION OF GLOBAL VARIABLES --- #
##########################################
DIGITS = "0123456789"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER = ALPHABET.upper()
ACCENTS = "àéè€ù£ç"
SPECIALS = "!@#$%^&*()-_+={}[]|\\:;\"',./<>?~` "
ALL = DIGITS+ALPHABET+ALPHABET_UPPER+ACCENTS+SPECIALS

CHARACTERS = {
    "a": ALL,
    "d": DIGITS,
    "l": ALPHABET,
    "L": ALPHABET_UPPER,
    "e": ACCENTS,
    "s": SPECIALS
}

##########################################
# --- Password list generator engine --- #
##########################################
def run_generator(filename:str, list_letters:list):    
    # --- Filename update if required --- #
    if f"{filename}.txt" in listdir("words_lists"):
        n = 1
        f = filename
        filename = f"{f}({n})"
        while f"words_lists/{filename}.txt" in listdir("words_lists"):
            # update of file name if it is not alone
            filename = f"{f}({n})"
            n += 1
            
    # --- Number of passwords to generate --- #
    nb_pwd_to_generate = 1

    for i in range(len(list_letters)):
        nb_possibilities = 0

        for letter in list_letters[i]:
            CHARACTERS.get(letter)
            # add the number of possibility of this carachter in the pwd
            nb_possibilities += len(CHARACTERS.get(letter))
        nb_pwd_to_generate *= nb_possibilities
    print(f"\n\n{Fore.MAGENTA}[PREPARATION] {nb_pwd_to_generate:,} passwords will be generated{Fore.RESET}")
    
    # --- Start of the algorithm --- #
    try:
        with tqdm(total=100, unit="%", bar_format='{percentage:3.0f}%|{bar}|') as pbar:

            with open(f"words_lists/{filename}.txt", "w") as f:
                progress_interval = round(0.01 * nb_pwd_to_generate)
                progress = 0

                def generate_passwords(n:int, list_letters:list, sequence="", nb_pwd=0):
                    """Returns a list of passwords
                    
                    :param n: lenght of the password
                    :param list_letters: list of possible values per character
                    """
                    nonlocal progress

                    # Length of password is reached
                    if n == 0:
                        progress += 1
                        if progress % progress_interval == 0:
                            pbar.update(1)
                            # print(f"{Fore.CYAN}[PROGRESS] {progress:,} passwords generated{Fore.RESET}")
                        f.write(sequence+"\n")
                        return nb_pwd + 1
                    else:
                        # --- Combination of set of characters --- #
                        characters = ""
                        for letter in list_letters[-n]:
                            characters += CHARACTERS.get(letter)
                        # --- Recursive calls --- #
                        for car in characters:
                            # n-1 stands for the lenght that needs to be added to complete a password
                            # we need to update the value of nb_pwd as it is returned
                            nb_pwd = generate_passwords(n - 1, list_letters, sequence + car, nb_pwd)
                        return nb_pwd

                nb_pwd = generate_passwords(len(list_letters), list_letters)
        print(f"{Fore.GREEN}The script has generated: {nb_pwd:,} passwords succesfully! {Fore.RESET}")
    
    except MemoryError:
        print(f"{Fore.RED}Out of memory! Please run the script on a PC with more RAM.{Fore.RESET}")
        raise MemoryError