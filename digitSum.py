def findSum(num:int)->int:
    if num%10 == num:
        return num
    else:
        return num%10 + findSum(num//10)

def magicNum(num:int)->bool:
    if num%10 == num:
        return num==1
    else:
        sum = 0
        while(num>0):
            sum += num%10
            num //= 10
        return magicNum(sum)

numSum = findSum(50113)
print(magicNum(50113))