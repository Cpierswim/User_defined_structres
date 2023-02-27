from linked_list import LinkedList
from binary_node import BinaryNode


class RunMain:
    def __init__(self) -> None:
        self.list = LinkedList()

    def append_nodes(self):
        print("\nAdd a new node with the value of 5")
        self.list.append(5)
        print("\nAdd a new node with the value of 10")
        self.list.append(10)
        print("\nAdd a new node with the value of 55")
        self.list.append(55)


    def find_values(self):
        print("\nSearch for a node with the value of 10")
        print(f"Node found: {self.list.contains(10)}")
        print("\nSearch for a node with the value of 22")
        print(f"Node found: {self.list.contains(22)}")

    def append_binary_nodes(self):
        print("\n\n===== Binary Tree: Insertion Activity =====")
        root = BinaryNode(27)
        root.insert(14)
        root.insert(35)
        root.insert(10)
        root.insert(19)
        root.insert(31)
        root.insert(42)
        #root.insert(22)

        print("\nSearch for node with value of 31")
        root.search_for_node(root, 31)
        print("\nSearch for node with value of 11")
        root.search_for_node(root, 11)

        print("\n===== Traversal Results =====") #This is mispelled in the lab
        print(f"In order traversal results: {root.inorder_traversal(root)}")
        print(f"Pre order traversal results: {root.preorder_traversal(root)}")
        print(f"Post order traversal results: {root.postorder_traversal(root)}")
        print("\n\n")

if __name__ == '__main__':
    main = RunMain()
    main.append_nodes()
    print(f"Length: {main.list.length}")
    main.find_values()

    print("----------------------\n\n")

    main.append_binary_nodes()