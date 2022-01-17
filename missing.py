from collections import Counter

key = Counter([1,2,2,3,4,5,6,7,5,6,7,8,9,10,12,1,23,4,54,4,67,19,10]) # hold the count of each of the elements present in the array
print([i for i in range(1, 70) if key[i] == 0])