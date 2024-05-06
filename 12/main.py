from terninator import caesar_cipher_encrypt, caesar_cipher_decrypt,  caesar_bruteforce

if __name__ == '__main__':
    message = input('Vvedite stroku: ')
    alphabet_size = 1104
    key = 1100

    # Дешифрование
    decrypted_message = caesar_cipher_decrypt(message, key, alphabet_size)
    print("Decrypted message:", decrypted_message)

    # Брутфорс атака на шифр
    caesar_bruteforce(message, alphabet_size)
