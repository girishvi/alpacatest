# Loop through each element in the list by checking the number of occurrences,
# then add them to a new set which will then print the duplicates.

myList  = [1,2,2,3,4,5,6,7,5,6,7,8,9,10,12,1,23,4,54,4,67,19,10];
newList = set()

for i in myList:
    if myList.count(i) >= 2: #more than 2 occurences, add to new list
        newList.add(i)

print(list(newList))
