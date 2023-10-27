from os import listdir


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
    from main import Color

    
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
    print(f"\n\n{Color.MAGENTA}[PREPARATION] {nb_pwd_to_generate:,} passwords will be generated{Color.RESET}")
    
    # --- Start of the algorithm --- #
    with open(f"words_lists/{filename}.txt", "w") as f:
        # TODO
        # small algo to determine the interval depeending on the nb pwd to generate
        progress_interval = 10000  # update every 100 pwd
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
                    print(f"{Color.CYAN}[PROGRESS] {progress:,} passwords generated{Color.RESET}")
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
        print(f"{Color.GREEN}The script has generated: {nb_pwd:,} passwords succesfully! {Color.RESET}")