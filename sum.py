def sumLis(lis,ptr=-1):
    lis[ptr] = lis[ptr] + 1
    if lis[ptr] > 9:
        lis[ptr] = 0
        ptr-=1
        if -ptr > len(lis):
            return sumLis([0] + lis,ptr)
        else:
            return sumLis(lis,ptr)
    return lis

for i in range(10):
    for j in range(10):
        lis = [i,j,9]
        print(f"{lis}\t\t{sumLis(lis)}")