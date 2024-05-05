def caesar_cipher_encrypt(message, key, alphabet_size):
    encrypted_message = []
    for letter in message:
        encrypted_message.append(chr((ord(letter) + key) % alphabet_size))
    return ''.join(encrypted_message)

def caesar_cipher_decrypt(encrypted_message, key, alphabet_size):
    decrypted_message = []
    for letter in encrypted_message:
        decrypted_message.append(chr((ord(letter) - key) % alphabet_size))
    return ''.join(decrypted_message)

def caesar_bruteforce(encrypted_message, alphabet_size):
    for i in range(alphabet_size):
        decrypted_message = []
        for letter in encrypted_message:
            decrypted_message.append(chr((ord(letter) - i) % alphabet_size))
        decrypted_message = ''.join(decrypted_message)
        print(f"Key: {i}, Decrypted message: {decrypted_message}")

if __name__ == '__main__':
    message = input('Vvedite stroku: ')
    alphabet_size = 1104
    key = 1100

    # # Шифрование
    encrypted_message = caesar_cipher_encrypt(message, key, alphabet_size)
    print("Encrypted message:", encrypted_message)

    # Дешифрование
    decrypted_message = caesar_cipher_decrypt(encrypted_message, key, alphabet_size)
    print("Decrypted message:", decrypted_message)

    # Брутфорс атака на шифр
    caesar_bruteforce(encrypted_message, alphabet_size)
