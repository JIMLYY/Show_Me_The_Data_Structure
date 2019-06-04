### Explanation for Problem 5: Blockchain
1. Data structure
Linked list
2. Explanation: the idea is simple: using linked list structure to link all blocks together. Because every block refers to previous block. Therefore, the first block has no block to refer to. I created a fucntion  create_primitive_block() for generating the first block. Then, the next_block function is used to generate a block based on previous one.
class blockchain is a wrapper to link all blocks together.

_Time complexity is O(1). Space complexity is O(n)._
