'''
set: unordered mutable unchangable

{}

-> duplication not allowed
'''

s1={1,2,3,4,5,6}
print(s1)
print(type(s1))

s2={1,5.6,9.00,"Khush",45,True}
print(s2)

s3={2,2,2,22,6,6,6,1,8,1,1,19,9,2,3,3}
print(s3)

print(len(s3))


# for i in s3:
#     print(i)

print(6 in s3)
print(23 in s3)


# add data

s3.add(34)
print(s3)

s3.add("Java")
print(s3)

s3.add(4+4j)
print(s3)

s3.update(s2)
print(s3)

l=['nihar','lamya','khush']
s3.update(l)
print(s3)

s3.remove('khush')
print(s3)

s3.discard('Java')
print(s3)

# s3.remove('abc')
s3.discard('abc')

print(s3.pop())
print(s3)

# s3.clear()
# print(s3)

# del s3
# print(s3)