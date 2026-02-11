lis = [1,0,2,1,5]

for i in range(len(lis)//2):
    if lis[i] == 0:
        lis[i],lis[-i] = lis[-i],lis[i]

print(lis)