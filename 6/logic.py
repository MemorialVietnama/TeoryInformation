import json
import heapq
from collections import defaultdict
from datetime import datetime
import os
import math


class HuffmanCoding:
    def __init__(self):
        self.huffman_code = None

    def generate_huffman_code(self, text):
        frequency = defaultdict(int)

        for char in text:
            frequency[char] += 1

        heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

        self.huffman_code = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    def save_huffman_code_to_json(self):
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        folder_name = f"{timestamp}"
        os.makedirs(folder_name, exist_ok=True)

        code_file_path = os.path.join(folder_name, "code.json")

        with open(code_file_path, "w") as code_file:
            json.dump(dict(self.huffman_code), code_file, ensure_ascii=False, indent=4)

        print(f"Huffman code saved in {code_file_path}")

    def decode_huffman(self, encoded_text):
        reversed_huffman_code = {code: char for char, code in dict(self.huffman_code).items()}
        decoded_text = ""
        current_code = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in reversed_huffman_code:
                decoded_text += reversed_huffman_code[current_code]
                current_code = ""

        return decoded_text


class HammingCoding:
    def __init__(self, word_size):
        self.word_size = word_size

    def encode(self, byte_array):
        encoded_bytes = bytearray()
        current_byte = 0
        bit_count = 0

        for byte in byte_array:
            for i in range(7, -1, -1):
                current_byte |= ((byte >> i) & 1) << bit_count
                bit_count += 1
                if bit_count == self.word_size:
                    encoded_bytes.append(current_byte)
                    current_byte = 0
                    bit_count = 0

        if bit_count > 0:
            encoded_bytes.append(current_byte)

        return encoded_bytes

    def decode(self, byte_array):
        decoded_bytes = bytearray()
        for byte in byte_array:
            for i in range(self.word_size - 1, -1, -1):
                decoded_bytes.append((byte >> i) & 1)

        return decoded_bytes

    def introduce_error(self, byte_array, error_position):
        byte_array[error_position // 8] ^= (1 << (error_position % 8))
        return byte_array

    def detect_error(self, byte_array):
        error_positions = []
        for i in range(len(byte_array) * 8):
            parity = 0
            for j in range(i, len(byte_array) * 8, i + 1):
                parity ^= ((byte_array[j // 8] >> (j % 8)) & 1)
            if parity != 0:
                error_positions.append(i)

        return error_positions


def read_settings_from_ini(filename):
    settings = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.split('=')
                settings[key.strip()] = int(value.strip())
    return settings


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('log.txt', 'a') as file:
        file.write(f"[{timestamp}] {message}\n")
    print(message)
