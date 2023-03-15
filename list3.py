'''
list comprehension


'''

# l=[2,3,4,5,6]

# print(l)

# for i in l:
#     print(i,end=" ")

# print('---------------')

# print([j for j in l])

# newList = [j*2 for j in l]
# print(newList)

# even = [i for i in l if i%2==0]
# print(even)

# l1 = [i for i in range(1,11)]
# print(l1)

# l2 = [i for i in range(1,11) if i%2!=0]
# print(l2)

# print([i for i in l2 if i>5 and i%3==0 ])


list = ['apple','kiwi','mango','banana','orange']
print(list)

print([i for i in list if i.count('w')>0])

print([i.upper() for i in list])

print([i for i in list if i.find('a')!=-1 ])


