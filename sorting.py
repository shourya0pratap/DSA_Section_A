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
        
def insertionSort(nums: list[int]):
    n = len(nums)
    for i in range(1, n):
        j = i - 1
        key = nums[i]
        
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
            
        nums[j+1] = key
        
def mergeSort(nums: list[int]):
    n = len(nums)
    if n <= 1:
        return nums
    mid = n//2
    leftHalf = nums[:mid]
    rightHalf = nums[mid:]
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    return merge(sortedLeft, sortedRight)

def merge(left: list[int], right: list[int]):
    m = len(left)
    n = len(right)
    result = []
    i = j = 0
    while i < m and j < n:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
    
def main():
    lis = [3,-1,2,4,0]
    print(mergeSort(lis))
    
main()