
def to_bin(text):
    return bytearray(text, 'utf-8')

def from_bin(data):
    return ''.join([int(data[i*8:i*8+8],2).to_bytes().decode() for i in range(int(len(data)/8))])

def bin(data, mode):
    result = ''
    if mode:
        result = to_bin(data)
    else:
        result = from_bin(data)
    
    return result