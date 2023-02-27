class BinaryNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        print(f"Node with value {value} created")

    def __str__(self) -> str:
        if self.value is not None:
            return str(self.value)
        else:
            return None
            

    def insert(self, value):
        if self.left is None and value <= self.value:
            
            self.left = BinaryNode(value)
            print(f"Node {self.value} updated with a left of {self.left} and a right of {self.right}")
        elif self.right is None and value > self.value:
            
            self.right = BinaryNode(value)
            print(f"Node {self.value} updated with a left of {self.left} and a right of {self.right}")
        elif self.left and value <= self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)
        
        #This i believe prints out the relation better, but I don't think I can use it since it doesn't match the requirements
        '''
        if self.left is not None and self.right is not None:
            print(f"Node {self.value} updated with a left of {self.left.value} and a right of {self.right.value}")
        elif self.left is not None:
            print(f"Node {self.value} updated with a left of {self.left.value} and a right of None")
        else:
            print(f"Node {self.value} updated with a left of None and a right of {self.right.value}")
        '''


    def search_for_node(self, node, value) -> bool:
        if node.value == value:
            print("Node Found!")
            return True
        elif value < node.value:
            print("Direction: Left")
            if node.left is not None:
                node.left.search_for_node(node.left, value)
            else:
                print("Node not found")
                return False
        else:
            print("Direction: Right")
            if node.right is not None:
                node.right.search_for_node(node.right, value)
            else:
                print("Node not found")
                return False
            
    def inorder_traversal(self, node):
        list = []
        if node.left is not None:
            left_list = node.inorder_traversal(node.left)
            list.extend(left_list)
        list.append(node.value)
        if node.right is not None:
            right_list = node.inorder_traversal(node.right)
            list.extend(right_list)
        return list
    
    def preorder_traversal(self, node):
        list = []
        list.append(node.value)
        if node.left is not None:
            left_list = node.preorder_traversal(node.left)
            list.extend(left_list)
        if node.right is not None:
            right_list = node.preorder_traversal(node.right)
            list.extend(right_list)
        return list
    
    def postorder_traversal(self, node):
        list = []
        
        if node.left is not None:
            left_list = node.postorder_traversal(node.left)
            list.extend(left_list)
        if node.right is not None:
            right_list = node.postorder_traversal(node.right)
            list.extend(right_list)
        list.append(node.value)
        return list