def partition(arr, low, high): # function to find the partition position 
	i = (low-1)		 # index of smaller element
	pivot = arr[high]	 # choose the rightmost element as pivot

# traverse through all elements
  # compare each element with pivot

	for j in range(low, high):
		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# increment index of smaller element
			i = i+1
            # swapping element at i with element at j
			arr[i], arr[j] = arr[j], arr[i]

  # swap the pivot element with the greater element specified by i
	arr[i+1], arr[high] = arr[high], arr[i+1]
      # return the position from where partition is done
	return (i+1)

# function to perform quicksort
def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
# find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
		pi = partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

arr = [1,2,2,3,4,5,6,7,5,6,7,8,9,10,12,1,23,4,54,4,67,19,10]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)