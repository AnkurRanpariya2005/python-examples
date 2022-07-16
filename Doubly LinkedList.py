class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class Doubly_LinkedList:
    def __init__(self):
        self.head = None

    def traverse_forward(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head       
            while n is not None:
                print(n.data, end="==>")
                n = n.nref
    
    def traverse_backward(self):
        print()
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head     
            while n.nref is not None:
                n = n.nref  
            while n is not None:
                print(n.data, end="<==")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LinkedList not empty")
    
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        if self.head is None:
            print("LinkedList is empty")
        
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                   break
                n = n.nref

            if n is None:
                print("Node is not found")

            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node
    
    def add_before(self, data, x):
        if self.head is None:
            print("LinkedList is empty")
        
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                   break
                n = n.nref
            if n is None:
                print("Node is not found")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
    
    def delete_begin(self):
        if self.head is None:
            print("LinkedList is empty")
        
        elif self.head.nref is None:
            self.head = None
        
        else:
            self.head = self.head.nref
            self.head.pref = None
                
    def delete_end(self):
        if self.head is None:
            print("LinkedList is empty")
        
        elif self.head.nref is None:
            self.head = None
        
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("LinkedList is empty")
            return
        
        if self.head.nref is None:
            if self.head == x:
                self.head = None
            else:
                print("Data is not found in Linkedlist")
            return
        
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("Data is not found in Linkedlist")


ll = Doubly_LinkedList()

ll.insert_empty(20)

ll.add_end(100)
ll.add_begin(10)

ll.add_after(30,20)
ll.add_after(110,100)

ll.add_before(15,20)
ll.add_before(5, 10)

ll.delete_begin()
ll.delete_end()
ll.delete_by_value(15)
ll.delete_by_value(100)

ll.traverse_forward()
ll.traverse_backward()