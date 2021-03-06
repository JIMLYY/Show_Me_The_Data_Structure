class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    union = set()
    node_1 = llist_1.head
    while node_1:
        union.add(node_1.value)
        node_1 = node_1.next
    node_2 = llist_2.head
    while node_2:
        union.add(node_2.value)
        node_2 = node_2.next

    union_list = LinkedList()
    for i in union:
        union_list.append(i)
    return union_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection_1 = set()
    node_1 = llist_1.head
    while node_1:
        intersection_1.add(node_1.value)
        node_1 = node_1.next
    intersection_2 = set()
    node_2 = llist_2.head
    while node_2:
        intersection_2.add(node_2.value)
        node_2 = node_2.next

    

    intersection = LinkedList()
    for i in intersection_1:
        if i in intersection_2:
            intersection.append(i)
    return intersection


# Test case 1
print("Test case 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("Union is... {}".format(union(linked_list_1,linked_list_2)))
print ("Intersection is... {}".format(intersection(linked_list_1,linked_list_2)))

# Test case 2
print("Test case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("Union is... {}".format(union(linked_list_3,linked_list_4)))
print ("Intersection is... {}".format(intersection(linked_list_3,linked_list_4)))

# Test case 3
print("Test case 3")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,5,6,100,101,102]
element_2 = [50,51,52]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("Union is... {}".format(union(linked_list_3,linked_list_4)))
print ("Intersection is... {}".format(intersection(linked_list_3,linked_list_4)))

