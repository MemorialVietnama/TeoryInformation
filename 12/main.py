#main.py
from multiprocessing import  Pool
from terninator import caesar_cipher_encrypt, caesar_cipher_decrypt,  caesar_bruteforce

if __name__ == '__main__':
    message = input('Введите строку: ')
    alphabet_size = 1104
    key = 1100

    with Pool(processes=3) as pool:
        encrypted_message = pool.apply(caesar_cipher_encrypt, (message, key, alphabet_size))
        decrypted_message = pool.apply(caesar_cipher_decrypt, (encrypted_message, key, alphabet_size))
        bruteforce_results = pool.apply(caesar_bruteforce, (encrypted_message, alphabet_size))

    print("Зашифрованное сообщение:", encrypted_message)
    print("Расшифрованное сообщение:", decrypted_message)
    for result in bruteforce_results:
        print(result)