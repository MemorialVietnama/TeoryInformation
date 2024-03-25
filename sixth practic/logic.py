import configparser
import logging
import random
import heapq
import collections 
import os
import logic

# Реализация кодирования по Хаффману
def huffman_encode(text):
    freq = collections.Counter(text)
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    huffman_dict = dict(sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))
    encoded_text = ''.join(huffman_dict[char] for char in text)
    
    # Преобразование закодированного текста в формат bytearray
    encoded_bytes = bytearray()
    for i in range(0, len(encoded_text), 8):
        byte = encoded_text[i:i+8]
        encoded_bytes.append(int(byte, 2))
    
    # Последовательность байтов в формате 0,1,0,0,0,1,1,1
    byte_sequence = ','.join(str(byte) for byte in encoded_bytes)
    
    return encoded_bytes, byte_sequence


# Функция для перевода текста в Юникод
def text_to_unicode(text):
    return ''.join([format(ord(char), '08b') for char in text])

# Функция для чтения настроек из файла settings.ini
def read_settings_from_ini(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config

class HammingCoder:
    def __init__(self, word_size):
        self.word_size = word_size

    def encode(self, byte_seq):
        encoded_seq = []
        for byte in byte_seq:
            encoded_byte = self._hamming_encode_byte(byte)
            encoded_seq.extend(encoded_byte)
        return encoded_seq

    def decode(self, byte_seq):
        decoded_seq = []
        for i in range(0, len(byte_seq), self.word_size):
            decoded_byte = self._hamming_decode_byte(byte_seq[i:i+self.word_size])
            decoded_seq.append(decoded_byte)
        return decoded_seq

    def _hamming_encode_byte(self, byte):
        encoded = []
        parity_indices = [2 ** i - 1 for i in range(self.word_size.bit_length())]
        data_bits = [byte >> i & 1 for i in range(self.word_size.bit_length() - 1, -1, -1)]
        
        while len(data_bits) < self.word_size - len(parity_indices):
            data_bits.insert(0, 0)
            
        for i in range(1, self.word_size + 1):
            if i in parity_indices:
                encoded.append(0)
            elif data_bits:
                encoded.append(data_bits.pop())
            else:
                encoded.append(0)
        for i, idx in enumerate(parity_indices):
            count = sum(encoded[j] for j in range(len(encoded)) if ((j + 1) >> i) & 1)
            encoded[idx] = int(count % 2 == 0)
        return encoded
    
    def _hamming_decode_byte(self, byte_seq):
        data_bits = []
        for i, bit in enumerate(byte_seq):
            if (i + 1) & (i + 1 + 1) != 0:  # Исправление здесь: изменил -1 на +1
                data_bits.append(bit)
        return sum(bit << i for i, bit in enumerate(data_bits[::-1]))





    
def decode_hamming_sequence():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    settings_file = os.path.join(current_directory, "settings.ini")  
    byte_sequence = input("Введите закодированную последовательность байт (разделенную запятыми): ").split(',')
    byte_sequence = [int(byte) for byte in byte_sequence]

    if os.path.exists(settings_file):
        settings = read_settings_from_ini(settings_file)
        word_size = int(settings.get('word_size', 8))
        hamming_coder = HammingCoder(word_size)
        decoded_sequence = hamming_coder.decode(byte_sequence)
        decoded_bytes = bytearray(decoded_sequence)  # Преобразуем список в bytearray
        print("Декодированная последовательность байт:", decoded_bytes)
    else:
        print(f"Файл настроек '{settings_file}' не найден.")







def text_to_unicode(text):
    # Реализация перевода текста в Unicode
    unicode_text = []
    for char in text:
        unicode_text.append(ord(char))
    return unicode_text

def huffman_encode(unicode_text):
    # Реализация кодирования текста по Хаффману
    freq = collections.Counter(unicode_text)
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    huffman_dict = dict(sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))
    encoded_text = ''.join(huffman_dict[char] for char in unicode_text)
    return encoded_text

def read_settings_from_ini(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config['Settings']  # Возвращает весь словарь настроек

def setup_logger():
    logging.basicConfig(filename='app.log', level=logging.INFO)
    return logging.getLogger()

def hamming_menu():
    while True:
        print("\nВыберите действие:")
        print("1. Внести ошибки в последовательность байт кода Хэмминга")
        print("2. Исправить ошибки в последовательности байт кода Хэмминга")
        print("3. Вернуться в главное меню")

        choice = input("Введите номер действия: ")

        if choice == "1":
            num_errors = int(input("Введите количество ошибок для внесения: "))
            byte_sequence = input("Введите закодированную последовательность байт (разделенную запятыми): ")
            byte_sequence = byte_sequence.split(",")
        elif choice == "2":
            logic.correct_errors(byte_sequence)
        elif choice == "3":
            print("Возвращение в главное меню.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из списка.")
