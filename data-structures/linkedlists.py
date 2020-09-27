#implementing singly LinkedLists in Python

#each node of a singly linkedlist must have a head and a tail
#the tail contains a pointer to the next element of the list
#the head is a value
class singleNode:
    def __init__(self, value, next=null):
        self.value = value
        self.next = next

class singleLinkedList:
    def __init__(self):
        self = singleNode(null)

    #adds a node with value VALUE to the beginning of the list.
    def addNodeBeginning(self, VALUE):
        if self.head == null:
            self.head = singleNode(VALUE)
        else:
            rest = self.tail
            self.head = singleNode(VALUE, rest)

    #tests whether or not a value exists inside the list.
    def contains(self, VALUE):
        pointer = self
        while pointer != null:
            if pointer.head == VALUE:
                return True
            else:
                pointer = pointer.tail
        return False

    #removes the first node with value VALUE inside the list.
    def remove(self, VALUE):
        pointer = self
        if not self.contains(VALUE):
            print("Item not in list")
            return None
        else:
            while pointer != null :
                if pointer.tail.head == VALUE:
                    pointer.tail = pointer.tail.tail
                pointer = pointer.tail
