class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def deleteAtLocation(self, location):
        if self.head is None:
            return  
        if location == 0:
            self.head = self.head.next
            return
        
        current = self.head
        for _ in range(location - 1):
            if current is None:
                return  
            current = current.next
        
        if current is None or current.next is None:
            return  
        
        
        current.next = current.next.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.head = Node(12)
ll.head.next = Node(56)
ll.head.next.next = Node(76)
ll.head.next.next.next = Node(11)
ll.head.next.next.next.next = Node(0)

print("Original list:")
ll.print_list()

ll.deleteAtLocation(0)  
print("After deleting at location 0:")
ll.print_list()

ll.deleteAtLocation(3)  
print("After deleting at location 3:")
ll.print_list()