class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.__root = None

    def insert(self, data):
        new_node = Node(data)
        p = self.__root
        while p:
            if data<p.data:
                if not p.left:
                    p.left = new_node
                    return
                p = p.left
            else:
                if not p.right:
                    p.right = new_node
                    return
                p = p.right
        self.__root = new_node
    
    def inorder(self):
        if self.__root:
            self.__rec_inorder(self.__root)
    
    def __rec_inorder(self, r):
        if r:
            self.__rec_inorder(r.left)
            print(r.data)
            self.__rec_inorder(r.right)

t = BST()
t.insert(5)
t.insert(3)
t.insert(1)
t.insert(4)
t.insert(7)
t.insert(6)
t.insert(9)
t.insert(10)
t.inorder()