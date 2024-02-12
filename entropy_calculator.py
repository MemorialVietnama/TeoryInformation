from collections import Counter
from math import log2

def calculate_alphabet_power(text):
    return len(set(text.lower()))

def calculate_hartley_entropy(alphabet_power):
    return alphabet_power

def calculate_shannon_entropy(text):
    text_length = len(text)
    frequencies = Counter(text.lower())
    probabilities = [freq / text_length for freq in frequencies.values()]
    shannon_entropy = -sum(p * (log2(p) if p > 0 else 0) for p in probabilities)
    return shannon_entropy

def calculate_redundancy(alphabet_power, shannon_entropy):
    hartley_entropy = calculate_hartley_entropy(alphabet_power)
    redundancy = (hartley_entropy - shannon_entropy) / hartley_entropy * 100
    return redundancy