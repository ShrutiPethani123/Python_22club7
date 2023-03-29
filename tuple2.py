t1=(1,2,3,4)
t2=('khush','lamya','nihar')

# x=tuple(zip(t1,t2))
x=tuple(zip(t2,t1))
print(x)


# unpack

t3=("Gujarat","Kerala","UP","GOA","Punjab","Hariyana","Tamilnadu")

# t2=('khush','lamya','nihar')

# a,b,c = t2
# print(a)
# print(b)
# print(c)


# a,b,*c = t3
# print(a)
# print(b)
# print(c)

# *a,b,c,d = t3
# print(a)
# print(b)
# print(c)
# print(d)

a,*b,c,d = t3
print(a)
print(b)
print(c)
print(d)

