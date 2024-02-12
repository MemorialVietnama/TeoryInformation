import math

def calculate_alphabet_size(text):
    return len(set(text.lower()))

def calculate_hartley_entropy(alphabet_size):
    return math.log2(alphabet_size)

def calculate_shannon_entropy(text):
    probabilities = [text.lower().count(c) / len(text) for c in set(text.lower())]
    return -sum(p * math.log2(p) for p in probabilities)

def calculate_alphabet_redundancy(hartley_entropy, shannon_entropy):
    return hartley_entropy - shannon_entropy / hartley_entropy * 100

def main(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    alphabet_size = calculate_alphabet_size(text)
    hartley_entropy = calculate_hartley_entropy(alphabet_size)
    shannon_entropy = calculate_shannon_entropy(text)
    redundancy = calculate_alphabet_redundancy(hartley_entropy, shannon_entropy)

    print(f"Alphabet Size: {alphabet_size}")
    print(f"Hartley Entropy: {hartley_entropy}")
    print(f"Shannon Entropy: {shannon_entropy}")
    print(f"Alphabet Redundancy: {redundancy:.2f}%")

if __name__ == "__main__":
    main("input.txt")  # Здесь файл можно изменить на ввод пользователя