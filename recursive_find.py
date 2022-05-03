class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        temp = self.root
        while temp:
            if temp.data>new_node.data:
                if temp.left == None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left
            elif temp.data<new_node.data:
                if temp.right == None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right

    def find(self,value,root=1):
        if root == 1:
            temp = self.root
        else:
            temp = root
        if temp is None:
            return False
        if temp.data == value:
            return True
        if value<temp.data:
            return self.find(value,temp.left) 
        if value > temp.data:
            return self.find(value,temp.right)
        
