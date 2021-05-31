#Quick Sort


def quick_sort(arr):
    less_than = []
    equal_to = []
    greater_than = []

    if len(arr) > 1:
        pivot = arr[len(arr) - 1]
        for num in arr:
            if num < pivot:
                less_than.append(num)
            elif num == pivot:
                equal_to.append(num)
            else:
                greater_than.append(num)    
        return quick_sort(less_than) + equal_to + quick_sort(greater_than)
    else:        
        return arr


# step 1 pick an element from the sorting_list to split it.
    # I am going to use the last element for now. I don't know if there is a "rignt" choice

#step 2 Split the sorting_list into two sorting_lists the pivot will go into the higher sorting_list again I don't think it makes a difference.  

#step 3 recursivly call the step 1 and 2 until all sub sorting_lists contain 3 or less items.

#step 4 return sorted values into aa new sorting_list
unsorted_list = [1,55,20,80,50,20,80,2,10,40]

print(*unsorted_list)
sorted_list = quick_sort(unsorted_list)
print(sorted_list)
