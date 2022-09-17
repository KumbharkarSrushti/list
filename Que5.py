list1=[[1, 2, 4], [2, 4, 4], [1, 2]]
i=0
sum=0
while i <len(list1):
    j=0
    sum1=0
    while j<len(list1[i]):
        sum1=sum1+list1[i][j]
        j=j+1
    i=i+1
    sum=sum+sum1
    print(sum1)
print("sum",sum)
