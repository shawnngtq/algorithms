class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def deleteNode(self, node1, node2):

        # When node to be deleted is head node
        if node1 == node2:
            if node1.next is None:
                return "There is only 1 node, the list can't be empty"

            # Copy the data of next node to head
            node1.data = node1.next.data

            # store address of next node
            node2 = node1.next

            # Remove the link of next node
            node1.next = node1.next.next
            return

        # When not first node, follow the normal deletion process
        # find the previous node
        prev = node1
        while prev.next and prev.next != node2:
            prev = prev.next

        if prev.next is None:
            print("The node to delete doesn't exist")

        prev.next = prev.next.next
        return

    def printList(self):
        temp = []
        current = self.head
        while current:
            temp.append(current.data)
            current = current.next
        print(temp)


llist = LinkedList()
llist.head = Node(12)
llist.head.next = Node(15)
llist.head.next.next = Node(10)
llist.head.next.next.next = Node(11)
llist.head.next.next.next.next = Node(5)
llist.head.next.next.next.next.next = Node(6)
llist.head.next.next.next.next.next.next = Node(2)
llist.head.next.next.next.next.next.next.next = Node(3)

llist.printList()
llist.deleteNode(llist.head, llist.head)
llist.printList()
llist.deleteNode(llist.head, llist.head.next.next)
llist.printList()
