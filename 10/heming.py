import math
import random
import time

class Heming:

    def __init__(self):
        pass

    def code(self, data, code_mode):

        lenght = 16

        if code_mode:
            s = ''.join(['{:0>8}'.format(str(bin(item))[2:]) for item in data])
            s += '0'*(lenght - (len(s) % lenght))

            powers = int(math.log2(lenght)) + 1

            result = ''

            for i in range(int(len(s) / lenght)):
                chunk = s[(i * lenght):((i + 1) * lenght)]

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
            powers = int(math.log2(lenght)) + 1
            lenght += powers

            result = ''

            for i in range(int(len(data) / lenght)):
                chunk = data[(i * lenght):((i + 1) * lenght)]
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
                        self.log.info(f"Была исправлена одна ошибка в чанке №{i + 1}!")

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
