class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    #appends in O(1) instead of O(n)
    def _append_node(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    #I wanted to use .apppend instead of .append_node, but didn't know if .append_node was required
    def append(self, value):
        self._append_node(value)

    #I feel like contains is a better method name than find_node, but I've included find_node if its required
    def contains(self, value) -> bool:
        return self.find_node(value) is not None
    
    def find_node(self, value) -> Node:
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            else:
                current_node = current_node.next
        return None