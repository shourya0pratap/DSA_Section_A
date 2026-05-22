lis = [31,33,34,35,38,39]
oddLis = []
evenLis = []

while lis:
    elem = lis.pop(0)
    if elem % 2 != 0:
        oddLis.append(elem)
    else:
        evenLis.append(elem)

while oddLis:
    lis.append(oddLis.pop(0))

while evenLis:
    lis.append(evenLis.pop(0))

print(lis)