# morse_decoder_encoder.py

import os

MORSE_CODE_DICT = {'А': '•-', 'Б': '-•••', 'В': '•--', 'Г': '--•', 'Д': '-••',
                  'Е': '•',  'Ж': '•••-', 'З': '--••', 'И': '••', 'Й': '•---',
                  'К': '-•-', 'Л': '•-••', 'М': '--', 'Н': '-•', 'О': '---',
                  'П': '•--•', 'Р': '•-•', 'С': '•••', 'Т': '-', 'У': '••-',
                  'Ф': '••-••', 'Х': '••••', 'Ц': '-•-•', 'Ч': '---•', 'Ш': '----',
                  'Щ': '--•-', 'Ъ': '--•--', 'Ы': '-•--', 'Ь': '-••-', 'Э': '••-••',
                  'Ю': '••--', 'Я': '•-•-', '0': '-----', '1': '•----', '2': '••---',
                  '3': '•••--', '4': '••••-', '5': '•••••', '6': '-••••', '7': '--•••',
                  '8': '---••', '9': '----•', '.': '•-•-•-', ',': '--••--', ';': '-•-•-•',
                  ':': '---•••', '?': '••--••', '!': '-•-•--', '-': '-••••-', ' ': '\t'}

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for char, morse in MORSE_CODE_DICT.items():
            if code == morse:
                text += char
    return text

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code.strip()
