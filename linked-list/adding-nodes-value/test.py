class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def sumLinkedListNodes(list1, list2):
  value1, value2 = '', ''
  head1, head2 = list1, list2

  while(head1 or head2):
    value1 += str(head1.data)
    head1 = head1.next
    value2 += str(head2.data)
    head2 = head2.next

  total = str(int(value1) + int(value2))

  totalList = list(total)

  list3 = {'head': Node(int(totalList[0]))}
  current = list3['head']

  for i in range(1, len(totalList)):
    current.next = Node(int(totalList[i]))
    current = current.next

  return list3


list1 = Node(5)
list1.next = Node(6)
list1.next.next = Node(3)

list2 = Node(8)
list2.next = Node(4)
list2.next.next = Node(2)

sumLinkedListNodes(list1, list2)