class Node:

  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def setNext(self, next):
    self.next = next

  def getValue(self):
    return self.value

  def getNext(self):
    return self.next


class LinkedList:

  def __init__(self):
    self.linkedList = {}
    self.head = None
    self.tail = None

  def addFirst(self, value):
    node = Node(value, self.head)

    self.head = node

  def addLast(self, value):
    node = self.head
    # one before the last one
    penultimate = None

    while node != None:
      penultimate = node
      node = node.getNext()

    newLastNode = Node(value)
    penultimate.setNext(newLastNode)

  def printValues(self):
    node = self.head

    while node != None:
      print(node.getValue())
      node = node.getNext()


myLinkedList = LinkedList()

myLinkedList.addFirst(11)
myLinkedList.addFirst(5)
myLinkedList.addFirst(10)
myLinkedList.addLast(100)
myLinkedList.printValues()

# 10 => 5 => 11 => 100
