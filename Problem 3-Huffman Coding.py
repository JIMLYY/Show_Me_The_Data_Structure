import sys
# calculate the frenqucies of the characters
def cal_freq(data):
    freqs = {}
    for char in data:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
    return sorted(freqs.items(), key = lambda item: item[1])

class Node:
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.parent = None
        self.freq = freq
    def isLeft(self):
        return self.parent.left == self

def Nodes(freq_list):
    return [Node(each) for each in freq_list]

def huffmanTree(nodes_list):
    queue = nodes_list[:]
    while len(queue) != 1:
        queue.sort(key = lambda node:node.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_parent = Node(node_left.freq + node_right.freq)
        node_parent.left = node_left
        node_parent.right = node_right
        node_left.parent = node_parent
        node_right.parent= node_parent
        queue.append(node_parent)
    return queue[0]

def huffman_encoding(nodes,root):
    length = len(nodes)
    codes = [""] * length
    for i in range(length):
        node = nodes[i]
        while node != root:
            if node.isLeft():
                codes[i] += "0"
            else:
                codes[i] += "1"
            node = node.parent
    return codes

def get_huffman(data,freqs,codes):
    huffman = ""
    for char in data:
        index = 0
        for each_tuple in freqs:
            if char == each_tuple[0]:
                huffman += codes[index]
                break
            index += 1 
    return huffman      
        
        
def huffman_decoding(huffman,freqs,codes):
    decoded_str=''
    while len(huffman) != 0:
        index = 0
        for code in codes:
            if code in huffman and huffman.index(code) == 0:
                decoded_str += freqs[index][0]
                huffman = huffman[len(code):]
                break
                print(huffman)
            index += 1
    return decoded_str
                

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
