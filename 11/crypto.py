from threading import Thread
from queue import Queue

class Crypt:

    thread = None
    orders = Queue()
    results = Queue()

    class Order:
        command = None
        value = None

    def processor(self, orders, results):
        while True:
            order = orders.get()
            m = order.value[0]
            k = order.value[1]
            n = order.value[2]
            c = []

            if order.command == 1:
                for letter in m:
                    c.append(chr((160 + ord(letter) + k) % n))
                c = ''.join(c)

            elif order.command == 2:
                for letter in m:
                    c.append(chr((ord(letter) - k - 160) % n))
                c = ''.join(c)
            else:
                break

            results.put(c)

    def crypt(self, msg, k, n):
        order = self.Order()
        order.command = 1
        order.value = (msg, k, n)

        self.orders.put(order)

        return self.results.get()
    
    def encrypt(self, msg, k, n):
        order = self.Order()
        order.command = 2
        order.value = (msg, k, n)

        self.orders.put(order)

        return self.results.get()

    def __init__(self):
        self.thread = Thread(target=self.processor, args=(self.orders, self.results))
        self.thread.start()

    def __del__(self):
        order = self.Order()
        order.command = 0
        order.value = (0, 0, 0)

        self.orders.put(order)

        self.thread.join()