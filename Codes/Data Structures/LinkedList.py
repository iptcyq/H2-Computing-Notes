class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, data):
        self.data = data
    def set_next(self, next):
        self.next = next

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        self.head = Node(data, self.head)
    def pop(self):
        if self.head == None:
            print("Error: list is empty")
        else:
            top = self.head
            self.head = top.get_next()
            return top.get_data()
    def count(self):
        ptr = self.head
        counter = 0
        while ptr:
            counter += 1
            ptr = ptr.get_next()
        return counter
    def display(self):
        ptr = self.head
        all_nodes = []
        while ptr:
            all_nodes.append(str(ptr.get_data()))
            ptr = ptr.get_next()
        print("[" + ", ".join(all_nodes) + "]")

    def insert(self, data, idx):
        if idx+1 > self.count() or idx < 0:
            print("Error: index out of range")
        elif idx == 0:
            self.push(data)
        else:
            ptr = self.head
            for i in range(idx):
                ptr = ptr.get_next()
            ptr.set_next(Node(data,ptr.get_next()))
    def remove(self, idx):
        if idx+1 > self.count() or idx < 0:
            print("Error: index out of range")
        if idx == 0:
            self.pop()
        else:
            ptr = self.head
            for i in range(idx-1):
                ptr = ptr.get_next()
            ptr.set_next(ptr.get_next().get_next())    
