inp = input("Enter array items: ")
nums = inp.split(" ")
nums = [int(x) for x in nums]
n = len(nums)

numMax = max(nums)
secMax = nums[0]

for i in range(n):
    if secMax < nums[i] and nums[i] < numMax:
        secMax = nums[i]
        
print(secMax)
