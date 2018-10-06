# Absolute values sum minimization

Given a sorted array of integers a, find an integer x from a such that the value of

`abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)`

is the smallest possible (here abs denotes the absolute value). If there are several possible answers, output the smallest one

## Algorithm
- To find the smallest abs sum, you need to select the element with the the middle value
- Since the given array is sorted, you just need to find the middle element

