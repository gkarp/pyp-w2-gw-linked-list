class AbstractLinkedList(object):
    """
    Abstract class representing the LinkedList inteface you must respect.
    
    You must not implement any of the method in this class, and this class
    must never be instantiated. It's just a "guide" of which methods
    the LinkedList class should respect.
    """

    def __str__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def append(self, element):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def pop(self, index=None):
        raise NotImplementedError()


class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

        

    def __str__(self):
        return '%s' % (self.elem)

    def __eq__(self, other):
        if type(self) == type(other):
            return self == other
        return False

    def __repr__(self):
        return "%s" % (self.elem)


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.elements = []      
        if (elements == None or len(elements) <1):
            #self.start, self.end = Node(None, None), Node(None, None)
            self.start, self.end = None, None
        if elements != None and len(elements) > 0:
            self.elements = elements
            index = 1
            for e in range(len(self.elements)):
                try:
                    e = Node(e, Node(self.elements[index]))
                except IndexError:
                    e = Node(e)
            try:
                self.start = Node(self.elements[0], self.elements[1])
                self.end = Node(self.elements[-1])
            except IndexError:
                self.start = Node(self.elements[0])
                self.end = self.start

        
        
    """
        self.elements = elements            #a lis
        if (self.elements == None or len(self.elements) <1):
            #self.start, self.end = Node(None, None), Node(None, None)
            self.start, self.end = None, None
        if self.elements != None and len(self.elements) > 0:
            index = 1
            for e in range(len(self.elements)):
                try:
                    e = Node(e, self.elements[index])
                except IndexError:
                    e = Node(e)
            self.start = self.elements[0]
            self.end = self.elements[-1]
    """
        
    """
        end_index = 1
        if self.elements != None:
            if len(self.elements) >= 1:
                self.start = self.elements[0]
                self.end = self.elements[-1]
                while end_index <= (len(self.elements)+1):
                    for i in elements:
                        try:
                        #if i != self.elements:
                            i = Node(i, self.elements[end_index])
                            end_index += 1
                            #print(end_index)
                        except IndexError:
                            i = Node(i)
                            break
                    break
    """
    """
        if len(self.elements) > 1:
            self.start = Node(self.elements[0], Node(self.elements[1]))             #Node pbject
            self.end = Node(self.elements[-1])
            
        if len(self.elements) == 1:
            self.start = Node(self.elements[0])             #Node pbject
            self.end = Node(self.elements[-1])
            
    """


    def __str__(self):
        if self.elements == None:
            return "[]"
        return "%s" % (self.elements)
        
    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        return self.elements
        
    def __getitem__(self, index):
        return self.elements[index]

    def __add__(self, other):
        if type(self) == type(other):
            return self.elements + other.elements

    def __iadd__(self, other):
        self.elements = self.elements + other.elements
        return self.elements

    def __eq__(self, other):
        return (self.elements) == other

    def append(self, elem):
        added_node = Node(elem, next = None)
        
        if self.elements != None:
            self.elements.append(added_node)
            #old_end = self.end
            #old_end.next = added_node
            #self.end = old_end
            #print(self.end, " = old end")
            #self.old_end = self.end
            #self.end = self.added_node
            #print(self.end, " added node")
            
            #self.old_end.next = self.added_node
            #self.elements.append(self.added_node)
         
            #print(s)
            #self.end = Node(self.end, added_node)

        #if (self.elements != None):
            
            #self.elements[-1] = Node(self.elements[-1], added_node)
            #self.end = added_node
            
           # self.end = self.added_node
        #else:
        if self.elements == None:
            self.elements = added_node
            self.start = added_node
            self.end = added_node

        
    
    def count(self):
        if self.elements != None:
            return len(self.elements)
        else:
            return 0
    

    def pop(self, index=None):
        if self.elements == None:
            raise IndexError
        output = None
        if index == None:
            output = self.elements[-1]
            del self.elements[-1]
        else:
            output = self.elements[index] 
            del self.elements[index]
        return output


#greg_list = LinkedList([1,2,4,5])
#greg_list.append(1000)
'''
greg_list = LinkedList()
greg_list.append(1000)
print(greg_list)
greg_list.append(2)
'''
greg_list = LinkedList([1,50])
greg_list.append(5000)
print(greg_list)
print(greg_list.start)
print(greg_list.start.next)

print(type((greg_list)))
print(type(greg_list.start))
print(type(greg_list[2]))
print(type((greg_list.start.next)))