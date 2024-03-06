#entropy_calculator.py
import math

def calculate_alphabet_size(text):
    return len(set(text.lower()))

def calculate_hartley_entropy(alphabet_size):
    return math.log2(alphabet_size)

def calculate_shannon_entropy(text):
    probabilities = [text.lower().count(char) / len(text) for char in set(text.lower())]
    return -sum(probabilities * math.log2(probabilities) for probabilities in probabilities)

def calculate_alphabet_redundancy(hartley_entropy, shannon_entropy):
    return hartley_entropy - shannon_entropy / hartley_entropy * 100

def calculate_entropy(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    alphabet_size = calculate_alphabet_size(text)
    hartley_entropy = calculate_hartley_entropy(alphabet_size)
    shannon_entropy = calculate_shannon_entropy(text)
    redundancy = calculate_alphabet_redundancy(hartley_entropy, shannon_entropy)

    return alphabet_size, hartley_entropy, shannon_entropy, redundancy
