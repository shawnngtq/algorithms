## [Add two numbers represented by linked lists | Set 2](http://www.geeksforgeeks.org/sum-of-two-linked-lists/)

Given two numbers represented by two linked lists, write a function that returns sum list. The sum list is linked list representation of addition of two input numbers. It is not allowed to modify the lists. Also, not allowed to use explicit extra space (Hint: Use Recursion).

**Examples**:
```
Input:
  First List: 5->6->3  // represents number 563
  Second List: 8->4->2 //  represents number 842
Output
  Resultant list: 1->4->0->5  // represents number 1405
```

**Algorithm**:
```
1. Find the number of both singly linked list
2. Find the sum of both the numbers
3. Create a new linked list based on the sum using for loop
```
