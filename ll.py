class Node:
    def __init__(self, data):
        self.data = data #the data of this node
        self.next = None #referring to the next node
        
class LinkedList:
    def __init__(self):
        self.head = None #the linked list head
        
    def printList(self):
        node = self.head
        while(node):
            print(node.data, end='->')
            node = node.next
            
    def insertEnd(self, data):  #insert only at the end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
            
if __name__ == "__main__":   #this will be true if you run `python ll.py` but false if you `import ll`
    ll = LinkedList()
    ll.head = Node("Chaky")
    
    #create some nodes
    node2 = Node("Chaky 2")
    node3 = Node("Chaky 3")
    
    #link these nodes to the ll
    ll.head.next = node2
    node2.next = node3
    
    #use a proper insert instead of manually insert like the two lines above
    ll.insertEnd("Chaky 4")
    
    #print the list
    ll.printList()
    
    
    
    