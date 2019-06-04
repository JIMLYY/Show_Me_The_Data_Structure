import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
      self.index = index
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash() 

    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = str(self.data).encode('utf-8') 
      sha.update(hash_str)
      return sha.hexdigest()
    
def create_primitive_block():
    time = datetime.datetime.now()
    return Block(0, time, "Primitive Transaction", "0")

def next_block(last_block):
    next_index = last_block.index + 1
    next_timestamp = datetime.datetime.now()
    next_data = "Transaction {}".format(next_index)
    next_hash = last_block.hash
    return Block(next_index, next_timestamp, next_data, next_hash)

class blockChain:
    def __init__(self):
        self.head = None
        self.last = None
    def append(self):
        if self.head is None:
            self.head = create_primitive_block()
            self.last = self.head
            return
        else:
            new_node = next_block(self.last)
            self.last = new_node
            
# Test 
a = blockChain()
a.append()
print(a.head.data)
print(a.last.data)
a.append()
print(a.head.data)
print(a.last.data)
a.append()
print(a.head.data)
print(a.last.data)

# Inspired by: 
# https://medium.com/@vishnuashok123/building-a-simple-blockchain-using-python-90d27ee50214



