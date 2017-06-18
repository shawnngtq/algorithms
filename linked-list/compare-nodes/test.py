# A linked list node structure
class Node:

  # Constructor to create a new node
  def __init__(self, key):
    self.char = key
    self.next = None


# This is not part of Node class
def compare(list1, list2):

  # Traverse both lists. Stop when either end of linked 
  # list is reached or current characters don't watch
  while(list1 and list2 and list1.char == list2.char):
    list1 = list1.next
    list2 = list2.next

  # If both lists are not empty, compare mismatching
  # characters 
  if(list1 and list2):
    return 1 if list1.char > list2.char else -1

  # If either of the two lists has reached end
  if (list1 and not list2):
    return 1

  if (list2 and not list1):
    return -1

  return 0


list1 = Node('g')
list1.next = Node('e')
list1.next.next = Node('e')
list1.next.next.next = Node('k')
list1.next.next.next.next = Node('s')
list1.next.next.next.next.next = Node('a')

list2 = Node('g')
list2.next = Node('e')
list2.next.next = Node('e')
list2.next.next.next = Node('k')
list2.next.next.next.next = Node('s')
list2.next.next.next.next.next = Node('b') 
 
print(compare(list1, list2))

list3 = Node('g')
list3.next = Node('e')
list3.next.next = Node('e')
list3.next.next.next = Node('k')
list3.next.next.next.next = Node('s')

print(compare(list1, list3))
print(compare(list3, list3))