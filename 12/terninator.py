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
    results = []
    for i in range(alphabet_size):
        decrypted_message = []
        for letter in encrypted_message:
            decrypted_message.append(chr((ord(letter) - i) % alphabet_size))
        decrypted_message = ''.join(decrypted_message)
        results.append(f"Key: {i}, Decrypted message: {decrypted_message}")
    return results
