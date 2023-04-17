'''
string: ordered and immutable -> ' ' or " "
list:   ordered and mutable -> []
tuple:  ordered and immutable -> ()

'''
# a="""
# dsjfnds
# gjsiudhf
# jgfusidah

# """

# print(a)

t = ('india','canada','japan','usa') 
print(t)

# duplicates allowed

t = ('india','canada','Japan','usa','india') 
print(t)


# length

print(len(t))
print(max(t))
print(min(t))

a = ('india')
print(type(a))

a = ('india',)
print(type(a))

b = (4.5)
print(type(b))

# data types
t1=(1,2,3,5)
t2=(False,True,True,False,False,False)
t3=(1,3,4,5.6,"java",True)
print(t1)
print(t2)
print(t3)

t = ('india','canada','Japan','usa','india') 
print(t)
print(t[0])
print(t[3])
print(t[-1])
print(t[-1:-3:-1])
print(t[2:5])
print(t[:4])


# change the value of tuple

# t[1]='Dubai'
# print(t)

# str = "Python"
# print(str[0])
# str[0]='j'
# print(str)

# l=[1,2,3,4]
# l[2]=5
# print(l)


l1 = list(t)
print(l1)
l1[1]='Dubai'
l1.append('Nepal')
l1.remove('usa')
print(l1)
t = tuple(l1)
print(t)


t1=('UK',)
t+=t1
print(t)

# del t1
# print(t1)

for i in t:
    print(i,end=" ")

print()

for i in range(len(t)):
    print(t[i],end=" ")
print()

i=0
while i<len(t):
    print(t[i],end=" ")
    i+=1
print()

t1=(1,2,3,4,5)
t2=('india', 'Dubai', 'Japan', 'india', 'Nepal', 'UK')

# t3=t1+t2
# print(t3)

# t3=t1*2
# print(t3)

# str="lamya"
# print(str*3)

# l=[1,2,3]
# print(l*2)

print(t3.count('india'))
print(t3.count(7))
# print(t3.count(1,3)) - invalid

print(t3.index('india'))





