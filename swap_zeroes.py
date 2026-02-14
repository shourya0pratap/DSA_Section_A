def swap_zeroes(lis):
    i = 0
    for j in range(len(lis)):
        if lis[j] != 0:
            lis[i] , lis[j] = lis[j] , lis[i]
            i+=1

lis = [0,1,2,3,0,4]
swap_zeroes(lis)
print(lis)