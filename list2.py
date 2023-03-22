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

# l5 = [3,6,8,7,4,5,2,6,9]
# l5.sort()
# print(l5)

# l5.sort(reverse=True)
# print(l5)

# l6=sorted(l5)
# print(l6)

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

8. Take one list from user and after that take range from user and delete all elements that contains in list from range.

    l= [1,2,3,5,1,5,45,7,85,8,9,6,4,7,8,]
    start:3
    end:9

    o/p: [1,2,1,45,85]
    
9. Take one list from user and remove all duplicate elements.

    l = [ 1,2,3,4,1,5,6,2,4]
    o/p: [1,2,3,4,5,6]

10. print list in reverse ordered.

11. print sum of digit in list.

    l = [12345,234,675,123,67]

    o/p:[15,9,18,6,13]

12. find cumulative sum.

    l = [1,3,4,5,6,7]
    o/p: [1,4,8,13,19,26]

13. Take one list from user and interchange first and last element.

    l = [1,3,4,5,6,7]
    o/p:[7,3,4,5,6,1]

14. Take one list from user and after that take one element from user and check that element is present in list or not.

    l = [1,3,4,5,6,7]

    ele: 3 -> Found at index 1
    ele: 2 -> Not Found

15. Input comma separated string convert into list and after that print sum of all element.

string - 1,2,4,5,6

l = [1,2,4,5,6]
sum: 18





'''
# 8.
# l=[]
# n=5

# for i in range(n):
#     l.append(int(input("Enter element: ")))

# # print(l)
# s=int(input("Enter starting range: "))
# e=int(input("Enter ending range: "))


# # for i in l:
# #     print(i)
# #     if i>=s and i<=e:
# #         l.remove(i)

# i=0
# while(i<len(l)):
#     if l[i]>=s and l[i]<=e:
#         l.remove(l[i])
#         i-=1
#     i+=1

# print(l)

# 9.

l=[]

for i in range(7):
    l.append(int(input("Enter a no: ")))

print(l)

# for i in range(0,len(l)):
#     if l.count(i)>1:
#         l.remove(i)
#         i-=1
# print(l)

l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)


