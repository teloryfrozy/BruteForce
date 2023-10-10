# --- DEFINITION OF GLOBAL VARIABLES --- #
CHARACTERS = {
    "d": "0123456789",
    "l": "abcdefghijklmnopqrstuvwxyz",
    "L": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "e": "àéè€ù£ç",
    "s": "!@#$%^&*()-_+={}[]|\\:;\"',./<>?~` "
}

def generate_sequences(n:int, list_letters:list, sequence="", list_code=[]):
    # Length of password is reached
    if n == 0:
        list_code.append(sequence)
    else:
        for car in CHARACTERS.get(list_letters[-n]):
            generate_sequences(n - 1, list_letters, sequence + car, list_code)

    return list_code


list_letters=['d', 'e']
print(generate_sequences(len(list_letters), list_letters))
