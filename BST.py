class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def insert(self,root,data):
        if root is None:
            newnode=Node(data)
            return newnode
        elif data<root.data:
            root.left=self.insert(root.left,data)
        elif data>root.data:
            root.right=self.insert(root.right,data)
        return root
    def preorder(self,root):
        if root is None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")
ob=BST()
root=None
root=ob.insert(root,10)
root=ob.insert(root,20)
root=ob.insert(root,5)
print("Preorder: ")
ob.preorder(root)
print("\nInorder: ")
ob.inorder(root)
print("\nPostorder: ")
ob.postorder(root)
















