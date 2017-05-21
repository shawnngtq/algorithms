### Given a linked list which is sorted, how will you insert in sorted way?

Initial linked list:
```2 -> 5 -> 7 -> 10 -> 5```

After insertion:
```2 -> 5 -> 7 -> 9 -> 10 -> 5```

**Algorithm**:
```
1) If linked list is empty then make the node as head and return it
2) If the value of the node inserted is smaller than the value of head node, 
then make the new node the new head
3) In a loop, put the new node(9) into appropriate position
```

Link: http://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/