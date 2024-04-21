import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import json
import os
import math
from collections import Counter
from heapq import heapify, heappush, heappop

class CodeGenerator:
    def __init__(self):
        # Инициализация объекта для генерации кодов Хаффмана
        self.codes = {}

    @staticmethod
    def calculate_entropy(file_path):
        # Рассчитывает энтропию текста в файле
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        total_chars = len(text)
        char_frequencies = {char: text.count(char) for char in set(text)}
        probabilities = [freq / total_chars for freq in char_frequencies.values()]

        entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
        return entropy

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

class MainWindow(tk.Tk):
    data: str = ''

    def __init__(self):
        super().__init__()
        self.title("Программа №8 ")
        self.iconbitmap("C:/git copy/TeoryInformation/8/main.ico")
        self.geometry('600x400+0+0')

        frame1 = tk.Frame(self, bg='white')
        frame1.pack(expand=True, fill='both')

        create_encode_button = tk.Button(frame1, text="Создать и закодировать текст", command=self.open_text_editor)
        create_encode_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        decode_button = tk.Button(frame1, text="Декодировать код Хаффмана", command=self.decode)
        decode_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        exit_button = tk.Button(frame1, text="Выход", command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def open_text_editor(self):
        self.text_editor_window = tk.Toplevel(self)
        self.text_editor_window.title("Выбор действия")

    # Создание переменной для хранения выбора пользователя
        self.action_choice = tk.StringVar(value="create_file")

    # Создание radiobutton для выбора действия "Просто создать текстовой файл"
        create_file_radio = tk.Radiobutton(self.text_editor_window, text="Просто создать текстовой файл", 
                                       variable=self.action_choice, value="create_file")

    # Создание radiobutton для выбора действия "Закодировать текстовой файл в JSON по Хаффману"
        encode_file_radio = tk.Radiobutton(self.text_editor_window, text="Закодировать текстовой файл в JSON по Хаффману", 
                                       variable=self.action_choice, value="encode_file")

    # Создание кнопки "Выбрать", которая будет вызывать соответствующую функцию в зависимости от выбора пользователя
        select_button = tk.Button(self.text_editor_window, text="Выбрать", command=self.perform_selected_action)

    # Размещение radiobutton и кнопки на окне
        create_file_radio.pack()
        encode_file_radio.pack()
        select_button.pack()

    def perform_selected_action(self):
    # Получение выбранного пользователем действия
        selected_action = self.action_choice.get()

        if selected_action == "create_file":
        # Если выбрано "Просто создать текстовой файл", вызываем функцию для открытия редактора текста
            self.open_text_editor_window()
        elif selected_action == "encode_file":
        # Если выбрано "Закодировать текстовой файл в JSON по Хаффману", вызываем функцию для кодирования в JSON
            self.encode_to_json()
        self.text_editor_window.destroy()

    def open_text_editor_window(self):
    # Функция для открытия редактора текста
        self.text_editor_window = tk.Toplevel(self)
        self.text_editor_window.title("Текстовый редактор")

        text_entry = tk.Text(self.text_editor_window, height=10, width=40)
        text_entry.pack(padx=10, pady=10)

        save_button = tk.Button(self.text_editor_window, text="Сохранить", command=lambda: self.save_text(text_entry.get("1.0", "end-1c")))
        save_button.pack()

    def encode_to_json(self):
    # Функция для кодирования текстового файла в JSON по Хаффману
        input_file = fd.askopenfilename(filetypes=[("Text files", "*.txt")])
        if input_file:
            output_file_path = fd.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
            if output_file_path:
                try:
                    cgen = CodeGenerator()
                    cgen.gen_code(input_file, output_file_path)

                # После успешного сохранения кода Хаффмана выводим информацию о шифровании
                    self.show_encryption_info(input_file, output_file_path)
                except Exception as e:
                    mb.showerror("Ошибка", f"Не удалось сохранить код Хаффмана: {e}")

    def show_encryption_info(self, input_file, output_file_path):
    # Функция для вывода информации о шифровании после сохранения кода Хаффмана в JSON
        with open(output_file_path, "r", encoding="utf-8") as json_file:
            json_content = json.load(json_file)
            encoded_text = json_content["binary_text"]

        encoded_file_size = os.path.getsize(output_file_path)
        entropy = CodeGenerator.calculate_entropy(input_file)
        average_bits_per_symbol = encoded_file_size * 8 / len(encoded_text)

        info_message = f"Исходный файл: {os.path.basename(input_file)}\n" \
                   f"Размер исходного файла: {os.path.getsize(input_file)} байт\n" \
                   f"Размер закодированного файла: {encoded_file_size} байт\n" \
                   f"Энтропия исходного текстового файла: {entropy}\n" \
                   f"Среднее количество бит на символ в закодированном файле: {average_bits_per_symbol:.2f}\n"
        mb.showinfo("Успех", f"Код Хаффмана успешно сохранен в файл: {output_file_path}")
        mb.showinfo("Информация о шифровании", info_message)


    def decode(self):
        # Пользователь выбирает файл JSON
        json_file_path = fd.askopenfilename(filetypes=[("JSON files", "*.json")])
        if json_file_path:
            try:
                # Загрузка данных из JSON файла
                with open(json_file_path, "r", encoding="utf-8") as json_file:
                    data = json.load(json_file)
                    encoded_text = data["binary_text"]
                    codes = data["codes"]

                # Раскодировка текста
                cgen = CodeGenerator()
                cgen.codes = codes
                decoded_text = cgen.decode_text(encoded_text)

                # Запрос пользователя на выбор имени файла для сохранения раскодированного текста
                output_file_path = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
                if output_file_path:
                    # Сохранение раскодированного текста в файл
                    with open(output_file_path, "w", encoding="utf-8") as output_file:
                        output_file.write(decoded_text)

                    # Вычисление параметров для вывода информации
                    input_file_size = os.path.getsize(json_file_path)
                    decoded_file_size = os.path.getsize(output_file_path)
                    entropy = CodeGenerator.calculate_entropy(output_file_path)
                    average_bits_per_symbol = decoded_file_size * 8 / len(encoded_text)
                    compression_ratio = input_file_size / decoded_file_size

                    # Формирование информационного сообщения
                    info_message = f"Исходный файл: {os.path.basename(json_file_path)}\n" \
                                   f"Размер исходного файла: {input_file_size} байт\n" \
                                   f"Размер раскодированного файла: {decoded_file_size} байт\n" \
                                   f"Энтропия исходного текстового файла: {entropy}\n" \
                                   f"Среднее количество бит на символ в закодированном файле: {average_bits_per_symbol}\n" \
                                   f"Степень сжатия: {compression_ratio:.2f}%"

                    # Вывод информации и сообщения об успешном завершении
                    mb.showinfo("Результат декодирования", info_message)
                    mb.showinfo("Успех", f"Раскодированный текст успешно сохранен в файл: {output_file_path}")

            except Exception as e:
                mb.showerror("Ошибка", f"Ошибка при декодировании: {e}")

    def exit_program(self):
        self.destroy()

if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
