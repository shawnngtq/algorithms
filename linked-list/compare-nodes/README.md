### Delete a given node in Linked List under given constraints

Given two linked lists, represented as linked lists (every character is a node in linked list). Write a function compare() that works similar to strcmp(), i.e., it returns 0 if both strings are same, 1 if first linked list is lexicographically greater, and -1 if second string is lexicographically greater.

**Examples**:
```
Input: list1 = g->e->e->k->s->a
       list2 = g->e->e->k->s->b
Output: -1

Input: list1 = g->e->e->k->s->a
       list2 = g->e->e->k->s
Output: 1

Input: list1 = g->e->e->k->s
       list2 = g->e->e->k->s
Output: 0
```

**Algorithm**:
```
1) If linked list is empty then make the node as head and return it
2) If the value of the node inserted is smaller than the value of head node, 
then make the new node the new head
3) In a loop, put the new node(9) into appropriate position
```

Link: http://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/