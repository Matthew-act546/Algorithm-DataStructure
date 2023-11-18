class Node:
    """The representation and inputting the nodes in the Linked List"""
    data = None 
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node Data: %s>" % self.data
    
class LinkedList:
    """Single line Linked List"""
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0                                                   
        while current: 
            count += 1 
            current = current.next_node

        return count
        
    def add(self, data):  
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """ 
        Insert a new node containing data and index postion 
        insertion takes 0(1) constant time but finding the node 
        at the insertion point takes 0(n) linear time

        Takes overall 0(n) time 
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)

            position = index
            current = self.head 

            while position > 1:
                current = current.next_node #<------------------------------------------------- i think error 
                position -= 1

            prev_node = current
            next_node = next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail : %s]" % current.data) 
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        return ' -> '.join(nodes)