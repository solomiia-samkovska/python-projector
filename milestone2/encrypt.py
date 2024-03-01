def encryption(message: str, key: int):

    encrypt_message = ""
 
    for char in message:
        if char.isupper(): 
            encrypt_message += letter_encryption(char, key, 'A')
            
        elif char.islower():
            encrypt_message += letter_encryption(char, key, 'a')
        else:
            encrypt_message += char
        
    return encrypt_message  

def letter_encryption(char, key, first_alphabet_letter: str):
    letter_index = ord(char) - ord(first_alphabet_letter)              # find the position in 0-25
    new_letter_index = (letter_index + key) % 26                       # new shifted position in 0-25
    new_letter_code = ord(first_alphabet_letter) + new_letter_index    # Unicode of the shifted position
    new_letter = chr(new_letter_code)                                  # encrypted letter
    return new_letter


print(encryption('The quick brown fox jumps over the lazy dog. 123!?', 1))