l = [1,2,3,[4,5,[12,34,15,67],7,8,9]]

# l[3][2].pop(1)
l[3][2].remove(34)
print(l)

# print(l)
# print(l[-1])
# print(l[-1][2])
# print(l[-1][-3])
# print(l[-1][-4][3])
# l[3][2].append(100)
# print(l)
# l[3][2].insert(3,50)
# print(l)

# print(l[0])
# print(l[3])
# print(l[3][1])
# print(l[3][2])

# for i in l[3]:
#     print(i,end=" ")

# print()
# print(l[3][2])
# print(l[3][2][2])

# for i in l[3][2]:
#     print(i,end=" ")


# l=[
#     [1,'ram',2000],
#     [2,'roy',2010],
#     [3,'joy',2008],
#     # [4,'jiya']
# ]

# for i in l:
#     print(i)

# for i,j,k in l:
#     print(i,j,k)

[
    [0,1,2,3,4],
    [0,1,2,3,4],
    [0,1,2,3,4],
    [0,1,2,3,4],
    [0,1,2,3,4]

]

l=[]
for i in range(4):
    l2=[]
    for j in range(4):
        l2.append(input("Enter element: "))
    l.append(l2)
print(l)
    