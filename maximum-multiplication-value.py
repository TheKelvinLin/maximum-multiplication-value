def maxProduct(nums):
    sortedNums = []
    result = 0
    sortedNums = sorted(nums, reverse = True) # Sort: from largest to smallest (reverse = True)
    result = sortedNums[0] * sortedNums[1] # Take the first element and multiply it with the second element to get the maximum value
    print(result)

maxProduct([4, 30, 1, 5])
maxProduct([15, -25, 0, 4])