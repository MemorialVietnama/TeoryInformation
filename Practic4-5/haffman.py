import json
from collections import Counter
from heapq import heapify, heappush, heappop
from datetime import datetime

class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        if other is None or not isinstance(other, Node):
            return NotImplemented
        return self.frequency < other.frequency


class CodeGenerator:
    def __init__(self):
        self.codes = {}

    def _build_heap(self, text):
        frequencies = Counter(text)
        heap = [Node(symbol=s, frequency=f) for s, f in frequencies.items()]
        heapify(heap)
        return heap

    def _build_tree(self, heap):
        while len(heap) > 1:
            left = heappop(heap)
            right = heappop(heap)

            internal_node = Node(frequency=left.frequency + right.frequency)
            internal_node.left = left
            internal_node.right = right

            heappush(heap, internal_node)

        return heap[0]

    def _generate_codes(self, node, code=""):
        if node.symbol:
            self.codes[node.symbol] = code
            return

        self._generate_codes(node.left, code + "0")
        self._generate_codes(node.right, code + "1")

    def gen_code(self, input_file_path, output_file_path):
        with open(input_file_path, "r", encoding="utf-8") as file:
            text = file.read()

        heap = self._build_heap(text)
        root = self._build_tree(heap)
        self._generate_codes(root)

        with open(output_file_path, "w", encoding="utf-8") as file:
            json.dump(self.codes, file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    cgen = CodeGenerator()
    cgen.gen_code("test.txt", "code.json")
