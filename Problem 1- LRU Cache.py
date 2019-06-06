import collections
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache_dic = {}
        self.cache_queue = collections.deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        # Pop the key from the current location and move it to the start of the queue
        if key in self.cache_queue:
            self.cache_queue.remove(key)
            self.cache_queue.append(key)
            return self.cache_dic[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if self.capacity == 0:
            self.capacity = 1
        if len(self.cache_queue) >= self.capacity:
            del self.cache_dic[self.cache_queue.popleft()]
        self.cache_dic[key] = value
        self.cache_queue.append(key)
        
# Test
our_cache_0 = LRU_Cache(0)
our_cache_0.set(1,1) # handle the corner case
print(our_cache_0.get(1))
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(1))       # print -1 and update self.cache_queue
print(our_cache.cache_queue )
print(our_cache.get(2))       # print 2 and update self.cache_queue
print(our_cache.cache_queue )
print(our_cache.get(5))       # print 5 and update self.cache_queue
print(our_cache.cache_queue )
print(our_cache.get(6))       # print 6 and update self.cache_queue
print(our_cache.cache_queue )
