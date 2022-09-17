# Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3




List2 = [-12, 14, 95, -3,-5]
positive=0
Negative=0
for num in List2:
    if num>=0:
        positive+=1
    else:
        Negative+=1
print("positive count is",positive)
print("Negative count is",Negative)

