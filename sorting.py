def bubbleSort(nums: list[int]):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]

def selectionSort(nums: list[int]):
    n = len(nums)
    for i in range(n-1):
        minInd = i
        for j in range(i+1, n):
            if nums[j] < nums[minInd]:
                minInd = j
        nums[i] , nums[minInd] = nums[minInd] , nums[i]