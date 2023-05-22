# Task 4.1 - should have been in .ipynb
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Task 4.2
class BSTree():
    def __init__(self, root=None):
        self.root = root

    def Insert(self, value, subnode=0):
        if self.root == None:
            self.root = TreeNode(value)
            return
        if subnode == 0:
            subnode = self.root
        if subnode.value > value:
            if subnode.left == None:
                subnode.left = TreeNode(value)
            else:
                self.Insert(value, subnode.left)
        elif subnode.value < value:
            if subnode.right == None:
                subnode.right = TreeNode(value)
            else:
                self.Insert(value, subnode.right)
        else:
            print(f"{value} already exists")
        
    def ReverseOrder(self, subnode=0):
        if subnode == 0:
            subnode = self.root
        if subnode != None:
            self.ReverseOrder(subnode.right)
            print(subnode.value)
            self.ReverseOrder(subnode.left)
    
    def Search(self, value, subnode=0):
        if subnode == 0:
            subnode = self.root
        if subnode.value == value:
            return True
        elif subnode.value > value:
            if subnode.left == None:
                return False
            else:
                return self.Search(value, subnode.left)
        elif subnode.value < value:
            if subnode.right == None:
                return False
            else:
                return self.Search(value, subnode.right)
            
    def Count(self, subnode=0):
        if subnode == 0:
            subnode = self.root
        if subnode != None:
            count = 1 #you can combine all these into 1 statement
            count += self.Count(subnode.left)
            count += self.Count(subnode.right)
        else:
            count = 0
        return count

# Task 4.3
file = open("Materials/Additional_Materials/INSERTTOTREE.txt")
data = file.read()
file.close()

data = data.split("\n")
bst = BSTree()
for item in data:
    bst.Insert(item)
print()

bst.ReverseOrder()
print(bst.Count())
print()

file = open("Materials/Additional_Materials/SEARCHINTREE.txt")
data = file.read()
file.close()

data = data.split("\n")
for item in data:
    exists = bst.Search(item)
    print(f"{item} exists") if exists else print(f"{item} does not exist")
