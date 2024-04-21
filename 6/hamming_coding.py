import bitarray

class HammingCoding:
    def __init__(self, word_size):
        self.word_size = word_size

    def calculate_num_parity_bits(self, word_size):
        num_parity_bits = 0
        while 2 ** num_parity_bits <= word_size + num_parity_bits + 1:
            num_parity_bits += 1
        return num_parity_bits
    
    def encode(self, text, word_size):
        # Преобразование текста в битовый массив
        bit_array = bitarray.bitarray()
        bit_array.frombytes(text.encode('utf-8'))

        # Дополнение нулями до кратности размера слова
        remainder = len(bit_array) % word_size
        if remainder != 0:
            bit_array.extend([0] * (word_size - remainder))

        # Кодирование по Хеммингу
        encoded_bits = self.hamming_encode(bit_array, word_size)

        # Преобразование последовательности битов в строку битов
        encoded_text = encoded_bits.to01()
        return encoded_text

    def decode(self, encoded_text, word_size):
        # Преобразование строки битов в битовый массив
        encoded_bits = bitarray.bitarray(encoded_text)

        # Декодирование по Хеммингу
        decoded_bits = self.hamming_decode(encoded_bits, word_size)

        # Преобразование битов в строку
        decoded_text = decoded_bits.tobytes().decode('utf-8').rstrip('\x00')
        return decoded_text

    def hamming_encode(self, bit_array, word_size):
        # Рассчитываем контрольные биты
        num_parity_bits = self.calculate_num_parity_bits(word_size)
        encoded_bits = bitarray.bitarray()

        # Заполняем битовый массив кодовыми битами и пустыми контрольными битами
        for i in range(num_parity_bits):
            encoded_bits.append(0)  # placeholder для контрольных бит
        j = 0  # индекс битов для оригинального сообщения
        k = 0  # индекс битов для закодированного сообщения

        # Заполняем кодовые биты и контрольные биты
        for i in range(len(bit_array) + num_parity_bits):
            # Если позиция бита - степень двойки, то это контрольный бит
            if i == (2 ** k - 1):
                k += 1  # переходим к следующему контрольному биту
                encoded_bits.insert(i, 0)  # вставляем пустой контрольный бит
            else:
                encoded_bits.insert(i, bit_array[j])  # вставляем кодовый бит
                j += 1  # переходим к следующему биту исходного сообщения

            # Вычисляем значение контрольных бит
        for i in range(num_parity_bits):
            index = 2 ** i - 1  # индекс текущего контрольного бита
            count_ones = 0
            # Проходим по всем битам, которые проверяет данный контрольный бит
            for j in range(index, len(encoded_bits), 2 * index + 1):
                for k in range(j, min(j + index + 1, len(encoded_bits))):
                    if encoded_bits[k]:
                        count_ones += 1
         # Устанавливаем контрольный бит в зависимости от количества единиц
            encoded_bits[index] = count_ones % 2

        return encoded_bits

    def hamming_decode(self, bit_array, word_size):
    # Рассчитываем количество контрольных битов в каждом блоке
        num_parity_bits = self.calculate_num_parity_bits(word_size)

    # Создаем битовый массив для декодированных данных
        decoded_bits = bitarray.bitarray()

    # Проходим по всем блокам кода
        for i in range(0, len(bit_array), word_size + num_parity_bits):
        # Копируем кодовые биты из текущего блока
            encoded_block = bit_array[i:i + word_size + num_parity_bits]
            decoded_block = bitarray.bitarray()

        # Проходим по кодовым битам и восстанавливаем информационные биты
            for j in range(word_size):
                if j not in [(2 ** k - 1) for k in range(num_parity_bits)]:
                    decoded_block.append(encoded_block[j])

        # Декодируем контрольные биты и исправляем ошибки
            for j in range(num_parity_bits):
                index = 2 ** j - 1  # Индекс текущего контрольного бита
                count_ones = 0
            # Подсчитываем количество единиц в блоке, проверяемом текущим контрольным битом
                for k in range(index, len(encoded_block), 2 * index + 1):
                    for l in range(k, min(k + index + 1, len(encoded_block))):
                        if l < len(decoded_block):  # Проверяем, что индекс не выходит за пределы длины блока
                            if encoded_block[l]:
                                count_ones += 1
            # Если количество единиц нечетное, то в блоке произошла ошибка
                if count_ones % 2 != 0:
                # Исправляем ошибку инверсией соответствующего бита
                    if index < len(decoded_block):  # Проверяем, что индекс не выходит за пределы длины блока
                        decoded_block[index] = not decoded_block[index]

        # Добавляем декодированные данные в общий битовый массив
            decoded_bits.extend(decoded_block)

        return decoded_bits


    
    