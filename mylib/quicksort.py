def quicksort(arr):
    #consider the base case
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] # choose this as pivot
        left = [x for x in arr[1:] if x < pivot] # move numbers lesser than pivot to left
        right = [x for x in arr[1:] if x >= pivot] # move numbers greater than pivot to right
    return quicksort(left) + [pivot] + quicksort(right) # merge all the elements and recurrsively call till len(arr) <= 1
