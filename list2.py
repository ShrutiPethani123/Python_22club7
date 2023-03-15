# Take one list from user and print that list.

# l1=[]
# n=int(input("Enter size of list: "))

# for i in range(n):
#     a = int(input("Enter a No:"))
#     l1.append(a)
    # l1.append(int(input("Enter a no: ")))

# print(l1)

# l2 = l1.copy()
# print(l2)

# l3=l1
# print(l3)

# print(id(l1))
# print(id(l2))
# print(id(l3))

# l3.append(45)

# print(l1)
# print(l3)
# print(l2)

# print(l1 is l2)
# print(l1 is l3)

# print(l1 is not l2)
# print(l1 is not l3)


# l1.clear()
# print(l1)
# print(l3)

# del l2
# print(l2)


l = [2,3,4,5,5,1,8,9]
l1 = ['c','c','cpp','java','java','java','python.','python','python','python']

# print(l1.count('java'))
# print(l.count(5))
# print(l1.count('j'))
# print(l1.count('python.'))

print(l1.index('java'))
# print(l1.rindex('python')) #not valid
print(l1.index('java',3))
# print(l1.index('php')) - error

l1.extend(l)
print(l1)

# l1.append(l)
# print(l1)

# l1.insert(0,'php')
# print(l1)

# l1[0]='java'
# print(l1)

# l1.remove('java')
# print(l1)

# l1.remove('php')    #error
# print(l1)

# l1.pop()
# print(l1)

# l1.pop(2)
# print(l1)

# l1.pop(-2)
# print(l1)

# l1.reverse() #reverse
# print(l1)

l5 = [3,6,8,7,4,5,2,6,9]
l5.sort()
print(l5)

l5.sort(reverse=True)
print(l5)

l6=sorted(l5)
print(l6)

'''
1. Take 5 number from user and add into list.
2. Take one list from user and print sum of all element.
3. Take one list from user and reverse that string and store that list in another list.
4. Take one list from user and find all even numbers into list.
5. Take two list from user and merge that two list into another list.

    l1 = [1,2,3,5]
    l2 =[6,2,3,4,5]
    l3 =[1,2,3,5,6,2,3,4,5]
6. Take one list from user and return list like this:

    l = [2,3,4,5]
    o/p: [4,9,16,25]

7. Take one list from user and print only lower case string element.

    list = ['java' , 'Python', 'JAVA','kiwi']
    



'''



