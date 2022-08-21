# given an array of integers that are out of orders determine the bounds of the smallest window
# that must be sorted in order for the entire array to be sorted
# for example given [3,7,5,6,9] should return  [1,3]


# this solution takes O(nlogn) time and n space , since we created a sorted copy of the original array.
def window(array):
    left , right= None , None
    array_copy_sorted = sorted(array)
    for i in range(len(array)):
        if array[i]!=array_copy_sorted[i] and left == None:
            left = i
        elif array[i]!=array_copy_sorted[i]:
            right = i
    return left , right

# this will take two passes over the array , operating in O(n) time and O(1) space
def window2(array):
    left , right= None , None
    max_seen_index=0
    min_seen_index=len(array)-1
    for i in range(len(array)):
        if array[i]>array[max_seen_index]:
            max_seen_index=i
        else:
            right=i
    for i in reversed(range(len(array))):
        if array[i]<array[min_seen_index]:
            min_seen_index=i
        else:
            left=i
        


    return left , right



print(window([3,7,5,4,2,6,10,4]))
print(window2([3,7,5,4,2,6,10,4]))