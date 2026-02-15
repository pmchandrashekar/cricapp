# def maxSubArrary(arr):
#     res = arr[0]
#     for i in range(len(arr)):
#         currentSum = 0
#         for j in range(i, len(arr)):
#             currentSum = currentSum + arr[j]
#             res = max(currentSum, res)
#     return res

# if __name__ == '__main__':
#     print(maxSubArrary([-1, 1, 1]))


# def maxProduct(arr):
#     n = len(arr)
  
#     # Initializing result
#     maxProd = arr[0]

#     for i in range(n):
#         mul = 1
      
#         # traversing in current subarray
#         for j in range(i, n):
#             mul *= arr[j]
          
#             # updating result every time
#             # to keep track of the maximum product
#             maxProd = max(maxProd, mul)
    
#     return maxProd

# if __name__ == "__main__":
    
#     arr = [-2, 1, 2]
    
#     print(maxProduct(arr))



def max_sub_array(arr):
    if 0 in arr:
        return 0
    
    res = arr[0]

    for i in range(len(arr)):
        currSum = 1
        for j in range(i, len(arr)):
            currSum = currSum * arr[j]
            res = max(currSum, res)

    return res    
if __name__ == "__main__":
    
    arr = [-2, 1, 2]
    
    print(max_sub_array(arr))


def max_sub_array(arr):
    if not arr or 0 in arr:
        return 0
    res = max(arr)
    cur_min, cur_max = 1, 1

    for n in arr:
        tmp = cur_max * n

        cur_max = max(n, cur_max*n, cur_min*n)
        cur_min = max(n, tmp, cur_min*n)
        
        res = max(res, cur_max)
    return res

if __name__ == "__main__":
    arr = [2, 2, 2]
    print(f"Max Product: {max_sub_array(arr)}") # Output: 4