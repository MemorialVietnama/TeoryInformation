from collections import Counter
from heapq import heapify, heappush, heappop
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

    def encode_text(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    def _build_heap(self, text):
        frequencies = Counter(text)
        heap = [Node(symbol=s, frequency=f) for s, f in frequencies.items()]
        heapify(heap)
        return heap

    def _build_tree(self, heap):
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
        if node.symbol:
            self.codes[node.symbol] = code
            return

        self._generate_codes(node.left, code + "0")
        self._generate_codes(node.right, code + "1")

    def gen_code(self, text):
        heap = self._build_heap(text)
        root = self._build_tree(heap)
        self._generate_codes(root)

        encoded_text = ''.join(self.codes[char] for char in text)

        return {"codes": self.codes, "binary_text": encoded_text}

    def decode_text(self, encoded_text):
        decoded_text = ""
        current_code = ""
        reverse_codes = {code: symbol for symbol, code in self.codes.items()}

        for bit in encoded_text:
            current_code += bit
            if current_code in reverse_codes:
                decoded_text += reverse_codes[current_code]
                current_code = ""

        return decoded_text