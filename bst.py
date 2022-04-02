from typing import Sized


class BinaryNode:
    def __init__(self,value) -> None:
        self.value=value
        self.left_child=None
        self.right_child=None
class BinaryTree:
    def __init__(self) -> None:
        self.root=None
    def insert(self,value) -> None:
        self.root=BinaryNode(value)
    

def _insert(node,value):
        if type(node)==BinaryTree:
                if(value<node.root.value):
                    if(node.root.left_child==None):
                        node.root.left_child=BinaryNode(value)
                    else:
                        _insert(node.root.left_child,value)
                else:
                    if(node.root.right_child==None):
                        node.root.right_child=BinaryNode(value)
                    else:
                        _insert(node.root.right_child,value)
        else:
            if(value<node.value):
                    if(node.left_child==None):
                        node.left_child=BinaryNode(value)
                    else:
                        _insert(node.root.left_child,value)
            else:
                    if(node.right_child==None):
                        node.right_child=BinaryNode(value)
                    else:
                        _insert(node.right_child,value)



                

binary=BinaryTree()
binary.insert(5)
_insert(binary,4)
_insert(binary,6)
_insert(binary,3)
print(binary.root.value)
print(binary.root.left_child.value)
print(binary.root.left_child.left_child.value)
print(binary.root.right_child.value)
lista=[1,2,3]
list = []
list.append(lista)
print(list)
