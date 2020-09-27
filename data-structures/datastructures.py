"""Linked lists have node objects linked together
They are easy to add to and remove from, but can only be
accessed sequentially.
"""

class listNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class basicLinkedList:
    def __init__(self):
        self.head = None

    def insertFront(value):
        if self.head == None:
            self.head = listNode(value, None)
        else:
            newNode = listNode(value, self.head)
            self.head = newNode

"""A tree is useful for searching and representing links
between data. Every node has some number of children.
Besides the root node, every node of the tree
has an arbitrary number of parents. Binary trees have
only two children per node. B-Trees can have way more.
Many tree algorithms lend themselves to being recursive, as every
node in a tree is also a tree in and of itself.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(value):
        if self.value:
            if self.value > value:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    #traverse the tree L -> root -> R
    def inOrderTraverse(self, root):
        returnList = []
        if root.value:
            returnList = self.inOrderTraverse(root.left)
            returnList.append(root.value)
            returnList = returnList + self.inOrderTraverse(root.right)
        return returnList

    #traverse the tree root -> L -> R
    def preOrderTraverse(self, root):
        returnList = []
        if root.value:
            returnList.append(root.value)
            returnList += self.preOrderTraverse(root.left)
            returnList += self.preOrderTraverse(root.right)
        return returnList

    #Post-order traversal not implemneted, but very similar

"""Graphs are more general implenetations of trees. While they
are not directly supported in Python, we can build them out of
dictionaries and lists.
"""

class dictGraph:
    def __init__(self, dict=None):
        if dict is None:
            dict = []
        self.dict = dict

    def getKeys(self): 
        return self.dict.keys()

    def getEdges(self):
        edgeList = []
        for k in self.getKeys():
            for v in self.dict[k]:
                if {k, v} not in edgeList:
                    edgeList.append({k, v})
        return edgeList

    def addVertex(self, value):
        if value not in self.dict:
            self.dict[k] = []

    def addEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.dict and vrtx2 in self.dict:
            self.dict[vrtx1].append(vrtx2)
            self.dict[vrtx2].append(vrtx1)
        else:
            self.dict[vrtx1] = vrtx2
            self.dict[vrtx2] = vrtx1

"""A trie is a type of tree that holds characters or
(perhaps even base pairs) within its nodes.
"""

class Trie:
    def __init__(self, words=None):
        self.root = dict()
        workDict = self.root
        if words is not None:
            for word in words:
                for char in word:
                    workDict = workDict.setdefault(letter, {})
                workDict[_end] = _end
        return self.root
