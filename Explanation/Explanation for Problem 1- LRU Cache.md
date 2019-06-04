### Explanation for Problem 1: LRU Cache
1. Data structure
In this problem, I use the hash table and queue.
2. For __get()__ function, in order to retrieve item from provided key(return -1 if nonexisten), I simply use hash table (dictionary in python).

_Time complexity is O(n). Space complexity is O(n)._
3. For __set()__ function, I use dictionary to store the data (key and value), and I use queue to keep track of length and the oldest item. When If the cache is at capacity remove the oldest item.

_Time complexity is O(1). Space complexity is O(1)._
