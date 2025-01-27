
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

def caesar_encrypt(plain_text):
    # Encrypted message
    cipher_text = ''
    # convert all letter in plain text to same case
    plain_text = plain_text.upper()
    # consider all letters in the plain_text
    for c in plain_text:
        # Find the numerical index for each plaintext letter in ALPHABET
        index = ALPHABET.find(c)
        # Update the index after shifting it with key size
        index = (index + KEY) % len(ALPHABET)

        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text
    

def caesar_decrypt(cipher_text):
    # Decrypted message
    plain_text = ''

    for c in cipher_text:
        index = ALPHABET.find(c)

        index = (index - KEY) % len(ALPHABET)

        plain_text = plain_text + ALPHABET[index]

    return plain_text


if __name__ == '__main__':
    
    message = 'Hello My name is Ayush'

    cipher = caesar_encrypt(message)
    print(cipher)

    plain = caesar_decrypt(cipher)
    print(plain)

