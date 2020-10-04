import numpy as np


m = np.array(
    [['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
     ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
     ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
     ['Sun', 13, 15, 19, 16]]
)

print(m.shape)
print(m)

print("Add row:")
m = np.append(m, [['Avg', 12, 15, 13, 11]], 0)
print(m)

print("Add column:")
m = np.insert(m, [5], [[1], [2], [3], [4], [5], [6], [7], [8]], 1)
print(m)

print("Delete row:")
m = np.delete(m, [len(m)-1], 0)
print(m)

print("Delete column:")
m = np.delete(m, np.s_[-1], 1)
print(m)
