# Original lists:
# ['0', '1', '2', '3', '4']
# ['red', 'green', 'black', 'blue', 'white']
# ['100', '200', '300', '400', '500']
# Concatenate element-wise three said lists:
# ['0red100', '1green200', '2black300', '3blue400', '4white500']

# a=['0', '1', '2', '3', '4']
# b=['red', 'green', 'black', 'blue', 'white']
# c=['100', '200', '300', '400', '500']
# d=[]
# i=0
# while i<len(a):
#     list=a[i]+b[i]+c[i]
#     d.append(list)
#     i=i+1
# print(d)

# a=[5,7,9,8,10,11,12,95]
# input=int(input("enter the num"))
# i=0
# count=0
# while i<len(a):
#     if input<a[i]:
#         count=count+1
#     i=i+1
# print(count)

a=[1,3,0,0,3,5,6]
# i=0
# b=[]
# c=[]
# while i <len(a):
#     if a[i]==0:
#         b.append(a[i])
#         # c=a[i].remove(b)
#     i=i+1
# print(b)
# print(a)
# print(c)
i=0
b=[]
c=[]
while i<len(a):
    if a[i]==0:
        b.append(a[i])
    i=i+1
print(b)