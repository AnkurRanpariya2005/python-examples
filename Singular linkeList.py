class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        n = self.head
        if n is None:
            print("LinkedList is empty")

        else:
            while n is not None:
                print(n.data, end="==>")
                n = n.ref

    def add_begin(self,data):
        node1 = Node(data)
        node1.ref = self.head
        self.head = node1
    
    def add_end(self,data):
        n = self.head
        node1 = Node(data)
        if n is None:
            self.head = node1
        
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = node1

    def add_afternode(self,data,x):
        n = self.head
        while n.ref is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("node is not present in Linked List")
        else:
            node1 = Node(data)
            node1.ref = n.ref
            n.ref = node1

    def add_beforenode(self,data,x):
        if self.head is None:
            print("Linked list is empty")

        elif self.head.data == x:
            node1 = Node(data)
            node1.ref = self.head
            self.head = node1

        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        
        if n.ref is None:
            print("Node is not found")

        else:
            node1 = Node(data)
            node1.ref = n.ref
            n.ref = node1

    
    
    def delete_begin(self):
        if self.head is None:
            print("LnkedList is empty")
        
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("LnkedList is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("LinkList is empty")

        elif self.head.data == x:
            self.head = self.head.ref
        
        else:
            n = self.head
            while n.ref is not None:
                if x == n.ref.data:
                    break
                n = n.ref

            if n.ref is None:
                print("Node is not present")
            
            else:
                n.ref = n.ref.ref

ll = LinkedList()
ll.add_begin(30)
ll.add_end(100)
ll.add_afternode(50,30)
ll.add_begin(20)
ll.add_begin(10)
ll.add_afternode(35,30)
ll.add_afternode(15,10)
ll.add_beforenode(5,10)
ll.add_beforenode(25,30)

ll.delete_begin()
ll.delete_end()
ll.delete_by_value(5)



ll.traverse()

