class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def nodePush(self, data):
    new_node = Node(data)
    if(self.head is None):
      self.head = new_node
    else:
      current = self.head
      while(current.next):
        current = current.next
      current.next = new_node

  def printList(self):
    temp = []
    current = self.head
    while(current):
      temp.append(current.data)
      current = current.next
    print(temp)


def mergeLinkedList(list1, list2):
  head1 = list1.head
  head2 = list2.head

  while(head1 and head2):
    next1 = head1.next
    next2 = head2.next

    head2.next = next1
    head1.next = head2

    head1 = next1
    head2 = next2

  list2.head = head2


list1 = LinkedList()
list1.nodePush(5)
list1.nodePush(7)
list1.nodePush(17)
list1.nodePush(13)
list1.nodePush(11)
list1.printList()

list2 = LinkedList()
list2.nodePush(12)
list2.nodePush(10)
list2.nodePush(2)
list2.nodePush(4)
list2.nodePush(6)
list2.printList()

list3 = LinkedList()

list4 = LinkedList()
list4.nodePush(1)
list4.nodePush(2)
list4.nodePush(3)

list5 = LinkedList()
list5.nodePush(4)
list5.nodePush(5)
list5.nodePush(6)
list5.nodePush(7)
list5.nodePush(8)

mergeLinkedList(list1, list2)
list1.printList()
list2.printList()
mergeLinkedList(list1, list3)
list1.printList()
list3.printList()
mergeLinkedList(list4, list5)
list4.printList()
list5.printList()
