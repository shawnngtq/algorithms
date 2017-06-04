### Longest Increasing Subsequence

The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.

**Examples**:
```
Input  : array[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : array[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : array[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}
```

**Algorithm**:
1) Let array[0..n-1] be the input array and L(i) be the length of the LIS ending at index i such that array[i] is the last element of the LIS.

2) Then, L(i) can be recursively written as:

- `L(i) = 1 + max( L(j) )` where `0 < j < i` and `array[j] < array[i]`
or
- `L(i) = 1`, if no such j exists.
To find the LIS for a given array, we need to return `max(L(i))` where `0 < i < n`.

Link: http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/