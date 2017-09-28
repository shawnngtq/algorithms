## [Binary Search](http://www.geeksforgeeks.org/binary-search/)

Given a sorted array of n elements, write a function to search a given element x in array

**Algorithms**:
```
1) Compare x with the middle element.
2) C1: if x matches with middle element, we return the mid index.
3) C2: x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
4) C3: x is smaller, recur for the left half.
```
