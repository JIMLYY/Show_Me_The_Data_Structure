import sys
# calculate the frequency of each character, which is to determine the priority of each character. 
def cal_freq(data):
    freqs = {}
    for char in data:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
    return sorted(freqs.items(), key = lambda item: item[1])

# construct class Node 
class TreeNode(object):
    def __init__(self,data):
        self.val = data[0]
        self.freq = data[1]
        self.left = None
        self.right = None
        self.parent = None
        self.code = ""
        
# construct class Node 
def Nodes(freq_list):
    return [TreeNode(each) for each in freq_list]

# define a method to insert a new node into the right position 
def add_to_Nodes(nodes, new_node):
    l = len(nodes)
    if l == 0:
        return [new_node]
    for i in range(l):
        if nodes[i].freq >= new_node.freq:
            nodes.insert(i,new_node)
            return nodes
    return nodes + [new_node]

# define nodeQueue, which has the function of add and pop
class nodeQueue(object):
    def __init__(self, freq_list):
        self.nodes = Nodes(freq_list)
        self.size = len(freq_list)

    def add(self,new_node):
        self.nodes = add_to_Nodes(self.nodes, new_node)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.nodes.pop(0)
    
# generate Huffman Tree
def huffmanTree(nodeQ):
    while nodeQ.size != 1:
        node1 = nodeQ.pop()
        node2 = nodeQ.pop()
        new = TreeNode([None, node1.freq + node2.freq])
        new.left = node1
        new.right = node2
        nodeQ.add(new)
    return nodeQ.pop()

huffman_encode = {}
huffman_decode = {}

# get huffman code for each characters 
def huffmanCode(root, ori_str):
    global codeDic, codeList
    if root:
        huffmanCode(root.left, ori_str+'0')
        root.code += ori_str
        if root.val:
            huffman_decode[root.code] = root.val
            huffman_encode[root.val] = root.code
        huffmanCode(root.right, ori_str+'1')
        
# get huffman code for whole string
def huffman_encoding(string):
    
    huffman_encoding_str = ""
    for char in string:
        huffman_encoding_str += huffman_encode[char]
    return huffman_encoding_str

# decode a huffman code into string 
def huffman_decoding(huffman_encoded_str):
    code = ""
    res = ""
    for char in huffman_encoded_str:
        code += char
        if code in huffman_decode:
            res += huffman_decode[code]
            code = ""
    return res


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    node_q = nodeQueue(cal_freq(a_great_sentence))
    tree = huffmanTree(node_q)
    huffmanCode(tree,"")
    encoded_data = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data)
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Reference: @ TomHawk's blog https://www.cnblogs.com/tomhawk/p/7471133.html  
