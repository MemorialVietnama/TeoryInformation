import random
import time
import math
from bitarray import bitarray
import heapq
class Haffman:

    class Node:

        def __init__(self, left, right):
            self.left = left
            self.right = right

    def __init__(self, text):
        letters = set(text)
        frequences = []
        for letter in letters:
            frequences.append((text.count(letter), letter))

        while len(frequences) > 1:
            frequences = sorted(frequences, key=lambda x: x[0], reverse=True)
            first = frequences.pop()
            second = frequences.pop()
            freq = first[0]+second[0]
            frequences.append((freq, self.Node(first[1], second[1])))

        self.code = {letter: '' for letter in letters}

        def walk(node, path=''):
            if isinstance(node, str):
                self.code[node] = path
                return
            walk(node.left, path + '0')
            walk(node.right, path + '1')

        walk(frequences[0][1])

    def get_codes(self):
        """Get result code"""
        return self.code

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_huffman_mapping(node, prefix="", mapping={}):
    if node:
        if node.char is not None:
            mapping[node.char] = prefix
        build_huffman_mapping(node.left, prefix + "0", mapping)
        build_huffman_mapping(node.right, prefix + "1", mapping)
    return mapping

def encode_huffman(text):
    root = build_huffman_tree(text)
    mapping = build_huffman_mapping(root)
    encoded_text = ''.join(mapping[char] for char in text)
    return encoded_text, mapping

def decode_huffman(encoded_text, mapping):
    reverse_mapping = {code: char for char, code in mapping.items()}
    decoded_text = ""
    code = ""
    for bit in encoded_text:
        code += bit
        if code in reverse_mapping:
            decoded_text += reverse_mapping[code]
            code = ""
    return decoded_text

class Heming:

    def __init__(self):
        pass

    def code(self, data, code_mode):

        length = 16

        if code_mode:
            s = ''.join(['{:0>8}'.format(str(bin(item))[2:]) for item in data])
            s += '0'*(length - (len(s) % length))

            powers = int(math.log2(length)) + 1

            result = ''

            for i in range(int(len(s) / length)):
                chunk = s[(i * length):((i + 1) * length)]

                for j in range(powers):
                    j = 2**j - 1
                    chunk = chunk[:j] + '0' + chunk[j:]

                for j in range(powers):
                    size = 2**j
                    j = size - 1
                    c = 0

                    while j < len(chunk):
                        c += chunk[j:(j + size)].count('1')

                        j += size * 2

                    j = size - 1
                    c %= 2

                    chunk = chunk[:j] + str(c) + chunk[j + 1:]

                result += chunk
        else:
            powers = int(math.log2(length)) + 1
            length += powers

            result = ''

            for i in range(int(len(data) / length)):
                chunk = data[(i * length):((i + 1) * length)]
                broken_bit_pos = 0

                for j in range(powers):
                    size = 2**j
                    j = size - 1
                    c = 0

                    while j < len(chunk):
                        c += chunk[j:(j + size)].count('1')

                        j += size * 2

                    j = size - 1
                    if int(chunk[j]):
                        c -= 1

                    c %= 2

                    if c != int(chunk[j]):
                        broken_bit_pos += j + 1

                    chunk = chunk[:j] + str(c % 2) + chunk[j + 1:]

                if broken_bit_pos:
                    if broken_bit_pos < len(chunk):
                        broken_bit_pos -= 1
                        print(f"Была исправлена одна ошибка в чанке №{i + 1}!")

                        inverted = int(not int(chunk[broken_bit_pos]))
                        chunk = chunk[:broken_bit_pos] + str(inverted) + chunk[broken_bit_pos + 1:]

                for j in reversed(range(powers)):
                    size = 2**j
                    j = size - 1

                    chunk = chunk[:j] + chunk[j + 1:]

                result += chunk

        return result

    def noise(self, data, errors_count):
        for i in range(errors_count):
            random.seed(i * time.time())
            pos = random.randint(0, len(data))

            inverted = int(not int(data[pos]))
            data = data[:pos] + str(inverted) + data[pos + 1:]

        return data

def crypt(codes, data):
    result = ''

    for letter in data:
        result += codes[letter]

    result = result + '0'*(8-(len(result)%8))
    output_bytes = bytearray([int(result[i*8:i*8+8],2) for i in range(int(len(result)/8))])

    return output_bytes

def encrypt(codes, data):
    result = ''

    while data:
        size_before = len(data)

        for k, v in codes.items():
            if data[0:len(v)] == v:
                result += k
                data = data[len(v):len(data)]

        if size_before == len(data):
            break

    return result
def text_to_unicode(text):
    return [str(ord(char)) for char in text]


def unicode_to_text(unicode_list):
    return ''.join(chr(int(code)) for code in unicode_list if code.isdigit())


def encode_unicode_huffman(unicode_text):
    encoded_text, mapping = encode_huffman(unicode_text)
    # Преобразуем отображение символов в строку
    mapping_str = {k: v for k, v in mapping.items()}
    mapping_bytes = str(mapping_str).encode('utf-8')
    return bytearray(encoded_text, 'utf-8'), mapping_bytes




def encode_bytearray_hamming(byte_array):
    heming = Heming()
    return heming.code(byte_array, True)

def decode_bytearray_hamming(encoded_bytes):
    heming = Heming()
    return heming.code(encoded_bytes, False)

def introduce_errors_hamming(encoded_bytes, errors_count):
    heming = Heming()
    return heming.noise(encoded_bytes, errors_count)

def introduce_errors_hamming(encoded_bytes, error_rate):
    # Определение количества битов, которые нужно изменить
    num_errors = int(len(encoded_bytes) * error_rate)

    # Генерация случайных позиций для ошибок
    error_positions = random.sample(range(len(encoded_bytes) * 8), num_errors)

    # Внесение ошибок
    for pos in error_positions:
        byte_index = pos // 8
        bit_index = pos % 8
        encoded_bytes[byte_index] ^= (1 << bit_index)

    return encoded_bytes

def correct_errors_hamming(encoded_bytes):
    # Подсчёт количества единичных битов в каждом байте
    error_counts = [bin(byte).count('1') for byte in encoded_bytes]

    # Позиции байтов с ошибками
    error_indices = [i for i, count in enumerate(error_counts) if count % 2 != 0]

    # Коррекция битов с ошибками
    for index in error_indices:
        encoded_bytes[index] ^= 1

    if len(error_indices) > 0:
        print("Были обнаружены и исправлены ошибки в байтах:", error_indices)
    else:
        print("Ошибок в байтах не обнаружено.")

    return encoded_bytes


def decode_huffman_to_unicode(encoded_text, mapping_bytes):
    try:
        # Преобразуем байты с картой кодирования Хаффмана в строку
        mapping_str = mapping_bytes.decode('utf-8')
        
        # Преобразуем строку обратно в словарь
        mapping = eval(mapping_str)
    except Exception as e:
        print("Error decoding mapping bytes:", e)
        return None

    if not isinstance(mapping, dict):
        print("Invalid mapping:", mapping)
        return None
    
    # Декодируем закодированный текст с использованием карты кодирования Хаффмана
    decoded_text = decode_huffman(encoded_text, mapping)
    
    return decoded_text


def decode_bytearray_hamming_to_unicode(encoded_bytes, mapping):
    # Декодирование с использованием кода Хемминга
    decoded_bytes = decode_bytearray_hamming(encoded_bytes)
    
    # Преобразование декодированных байтов в текст
    unicode_text = decode_huffman_to_unicode(decoded_bytes, mapping)
    
    return unicode_text


def decode_huffman(encoded_text, mapping):
    reverse_mapping = {code: char for char, code in mapping.items()}
    decoded_text = ""
    code = ""
    for bit in encoded_text:
        code += bit
        if code in reverse_mapping:
            decoded_text += str(reverse_mapping[code])  # Ensure decoded text is a string
            code = ""
    return decoded_text


