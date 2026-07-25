class Node:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:


    def __init__(self, capacity: int):
        self.val_to_node = {}
        self.node_to_val = {}
        self.key_val = {}
        self.capacity = capacity

        self.size = 0
        self.head = None
        self.tail = None
        

    def insert(self, val):

        if self.size == self.capacity:
            self.remove(self.tail)

        node = Node(val)
        node.next = self.head

        if self.head:
            self.head.prev = node

        self.head = node

        if not self.tail:
            self.tail = node

        self.size += 1
        
        self.val_to_node[val] = node
        self.node_to_val[node] = val
        return node

    def remove(self, node):
        if self.tail == node:
            self.tail = node.prev

        if self.head == node:
            self.head = node.next

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev
        
        self.size -= 1

        val = self.node_to_val[node]

        del self.node_to_val[node]
        del self.val_to_node[val]
        

        

    def get(self, key: int) -> int:
        if key in self.val_to_node:
            self.remove(self.val_to_node[key])
            self.insert(key)
            return self.key_val[key]

        return -1   


    def put(self, key: int, value: int) -> None:

        if key in self.val_to_node:
            self.remove(self.val_to_node[key])
        
        self.insert(key)   

        self.key_val[key] = value

        
