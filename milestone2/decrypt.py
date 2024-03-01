def decryption(message: str, key: int):

    decrypt_message = ""
 
    for char in message:
        if char.isupper(): 
            decrypt_message += letter_decryption(char, key, 'A')
            
        elif char.islower():
            decrypt_message += letter_decryption(char, key, 'a')
        else:
            decrypt_message += char
        
    return decrypt_message  

def letter_decryption(char, key, first_alphabet_letter: str):
    letter_index = ord(char) - ord(first_alphabet_letter)              # find the position in 0-25
    new_letter_index = (letter_index - key) % 26                       # new shifted position in 0-25
    new_letter_code = ord(first_alphabet_letter) + new_letter_index    # Unicode of the shifted position
    new_letter = chr(new_letter_code)                                  # encrypted letter
    return new_letter


print(decryption("Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.'#%', 098", 1))