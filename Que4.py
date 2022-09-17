list1=[[1, 2, 4], [2, 4, 4], [1, 2]]
i=0
b=[]
while i <len(list1):
    j=0
    max1=list1[i][j]
    while j<len(list1[i]):
        if max1<list1[i][j]:
            max1=list1[i][j]
            b.append(max1)
        j=j+1
    i=i+1
print(b)
