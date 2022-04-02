from typing import ValuesView


class BinaryNode:
    def __init__(self,value) -> None:
        self.value=value
        self.left_child=None
        self.right_child=None
    def is_leaf(self):
        if(self.left_child==None and self.right_child==None):
            return "jest lisciem"
        return "nie jest lisciem"
    def add_left_child(self,value):
        self.left_child=BinaryNode(value)
    def add_right_child(self,value):
        self.right_child=BinaryNode(value)
    def traverse_pre_order (self):
        print(self.visit())
        if(self.left_child!=None):
            self.left_child.traverse_pre_order()
        if(self.right_child!=None):
            self.right_child.traverse_pre_order()
    def visit(self):
        return self.value
    def traverse_in_order (self):
        
        if(self.left_child!=None):
            self.left_child.traverse_in_order()
        print(self.visit())
        if(self.right_child!=None):
            self.right_child.traverse_in_order()
    def traverse_post_order (self):
        
        if(self.left_child!=None):
            self.left_child.traverse_post_order()
        
        if(self.right_child!=None):
            self.right_child.traverse_post_order()
        print(self.visit())

class BinaryTree:
    def __init__(self,value) -> None:
        self.root=BinaryNode(value)
    def add_left_child(self,value):
        self.root.add_left_child(value)
    def add_right_child(self,value):
        self.root.add_right_child(value)
    def traverse_in_order (self):
        self.root.traverse_in_order()
    def traverse_pre_order (self):
        self.root.traverse_pre_order()
    def traverse_post_order (self):
        self.root.traverse_post_order()
   

            
        



# tree=BinaryNode(10)
# tree.add_left_child(9)
# tree.add_right_child(2)
# tree.left_child.add_left_child(1)
# tree.left_child.add_right_child(3)
# tree.right_child.add_left_child(4)
# tree.right_child.add_right_child(6)
# print(tree.is_leaf())
# # tree.traverse_pre_order()
# tree.traverse_in_order()
# print("+++++++")
# tree.traverse_post_order()
# print("---------")
# tree.traverse_pre_order()
tree=BinaryTree(10)
tree.add_left_child(9)
tree.add_right_child(2)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.right_child.add_left_child(4)
tree.root.right_child.add_right_child(6)
tree.traverse_in_order()
print("++++++++++++++++++++")
tree.traverse_post_order()
print("++++++++++++++++++++")
tree.traverse_pre_order()