import os
import argparse
from haffman import CodeGenerator
from datetime import datetime

def create_code_folder():
    folder_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    os.makedirs(folder_name)
    return folder_name

def main():
    parser = argparse.ArgumentParser(description="Huffman Code Generator CLI")
    parser.add_argument("input_file", help="Путь к файлу для кодирования")

    args = parser.parse_args()

    cgen = CodeGenerator()
    code_folder = create_code_folder()
    code_file_path = os.path.join(code_folder, "code.json")

    try:
        cgen.gen_code(args.input_file, code_file_path)
        print(f"Код Хаффмана сохранен. Код сохранен в файле: {code_file_path}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
