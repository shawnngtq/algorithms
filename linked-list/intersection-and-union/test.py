class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def printList(self):
    temp = []
    current = self.head
    while(current):
      temp.append(current.data)
      current = current.next
    print(temp)

  def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

# A utilty function that returns true if data is present
# in linked list  else return false
def isPresent(head, data):
  t = head

  # When reference head matches the data, return true
  while (t is not None):
    if(t.data == data):
      return True
    t = t.next
  return False

# Function that gets the same data in 2 linked lists
def getIntersection(head1, head2):
  result = []
  t1 = head1

  while(t1 is not None):
    if(isPresent(head2, t1.data)):
      result.append(t1.data)
    t1 = t1.next
  return result

# Function that gets the union of 2 linked lists
# without duplicates
def getUnion(head1, head2):
  result = []
  t1, t2 = head1, head2

  # Add everything in linked list 1 to result
  while(t1 is not None):
    result.append(t1.data)
    t1 = t1.next

  # Add non-duplicate data from linked list 2
  # to result
  while(t2 is not None):
    if not (isPresent(head1, t2.data)):
      result.append(t2.data)
    t2 = t2.next
  return result


list1 = LinkedList()
list1.push(20)
list1.push(4)
list1.push(15)
list1.push(10)
list1.printList()

list2 = LinkedList()
list2.push(10)
list2.push(2)
list2.push(4)
list2.push(8)
list2.printList()

print('Intersection: ', getIntersection(list1.head, list2.head))
print('Union: ', getUnion(list1.head, list2.head))