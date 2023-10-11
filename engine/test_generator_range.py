# --- DEFINITION OF GLOBAL VARIABLES --- #
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


def run_generator(filename:str):
    with open(f"{filename}.txt", "w") as f:
        def generate_passwords(n:int, list_letters:list, sequence="", nb_pwd=0):
            """Returns a list of passwords
            
            :param n: lenght of the password
            :param list_letters: list of possible values per character
            """
            # Length of password is reached
            if n == 0:
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
        
        list_letters=['L', 'l', 'l', 'l', 's', 'd', 'd', 'd', 'd']
        nb_pwd = generate_passwords(len(list_letters), list_letters)
        print(f"The script has generated: {nb_pwd} passwords succesfully!")

print(r"[a-z]")
print(r"[0-9]")
run_generator("words_list")
# ?L?l?l?l?s?d?d?d?d
# ?l?d?l?d?d?d?d?d