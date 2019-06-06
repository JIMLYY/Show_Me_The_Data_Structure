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

class BlockChain:
    def __init__(self):
        self.head = create_primitive_block()
        self.last = self.head
    def append(self):
        if self.head is None:
            self.head = create_primitive_block()
            self.last = self.head
            return
        else:
            new_node = next_block(self.last)
            self.last = new_node
            
# Test Cases
# corner case test (initiating the BlockChain() object but not adding anything)
blockChain = BlockChain()
print ("The first block was created at {}".format(blockChain.head.timestamp))
print ("Let's add a new block!")
blockChain.append()
print("Now, the head is {}".format(blockChain.head.data))
print("The tail is {}".format(blockChain.last.data))
print ("Let's add a new block, again!")
blockChain.append()
print("Now, the head is still {}".format(blockChain.head.data))
print("The tail is updated, which is {}.".format(blockChain.last.data))
print ("Let's...I promise, this is the last addition. LOL")
blockChain.append()
print("The head is ...{}".format(blockChain.head.data))
print("The tail is updated...{}".format(blockChain.last.data))

# Inspired by: 
# https://medium.com/@vishnuashok123/building-a-simple-blockchain-using-python-90d27ee50214



