import json
from collections import Counter
from heapq import heapify, heappush, heappop
import math

def calculate_entropy(file_path):
    # Рассчитывает энтропию текста в файле
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    total_chars = len(text)
    char_frequencies = {char: text.count(char) for char in set(text)}  # Создание словаря частот символов
    probabilities = [freq / total_chars for freq in char_frequencies.values()]  # Рассчет вероятностей
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)  # Рассчет энтропии
    return entropy

class Node:
    def __init__(self, symbol=None, frequency=None):
        # Класс для представления узла в дереве Хаффмана
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        # Метод сравнения для сравнения узлов по частоте
        if other is None or not isinstance(other, Node):
            return NotImplemented
        return self.frequency < other.frequency

class CodeGenerator:
    def __init__(self):
        # Инициализация объекта для генерации кодов Хаффмана
        self.codes = {}

    def encode_text(self, text):
        # Кодирует текст с использованием созданных кодов
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    def print_codes(self):
        # Выводит на экран созданные коды
        encrypted_sentence = ""
        for symbol, code in self.codes.items():
            print(f"Шифровка: {code} {symbol if symbol.isalpha() else ''}")
            encrypted_sentence += code
        print(f"Шифрованное предложение: {encrypted_sentence}")

    def _build_heap(self, text):
        # Строит кучу (min-heap) для частот символов
        frequencies = Counter(text)
        heap = [Node(symbol=s, frequency=f) for s, f in frequencies.items()]
        heapify(heap)
        return heap

    def decode_file(self, encoded_text, output_file_path):
        # Раскодирует текст и записывает результат в файл
        decoded_text = self.decode_text(encoded_text)
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(decoded_text)

    def _build_tree(self, heap):
        # Строит дерево Хаффмана из кучи (min-heap)
        heapify(heap)
        while len(heap) > 1:
            left = heappop(heap)
            right = heappop(heap)

            internal_node = Node(frequency=left.frequency + right.frequency)
            internal_node.left = left
            internal_node.right = right

            heappush(heap, internal_node)

        return heap[0]

    def _generate_codes(self, node, code=""):
        # Рекурсивно генерирует коды Хаффмана для символов
        if node.symbol:
            self.codes[node.symbol] = code
            return

        self._generate_codes(node.left, code + "0")
        self._generate_codes(node.right, code + "1")

    def gen_code(self, input_file_path, output_file_path):
        # Генерирует код Хаффмана для текста в файле и сохраняет его в файл
        with open(input_file_path, "r", encoding="utf-8") as file:
            text = file.read()

        heap = self._build_heap(text)
        root = self._build_tree(heap)
        self._generate_codes(root)

        binary_codes = {char: self.codes[char] for char in text}

        encoded_text = ''.join(binary_codes[char] for char in text)

        with open(output_file_path, "w", encoding="utf-8") as file:
            json.dump({"codes": self.codes, "binary_text": encoded_text}, file, ensure_ascii=False, indent=2)

    def decode_text(self, encoded_text):
        # Декодирует текст из бинарной строки в символьную строку
        decoded_text = ""
        current_code = ""
        reverse_codes = {code: symbol for symbol, code in self.codes.items()}

        for bit in encoded_text:
            current_code += bit
            if current_code in reverse_codes:
                decoded_text += reverse_codes[current_code]
                current_code = ""

        return decoded_text
