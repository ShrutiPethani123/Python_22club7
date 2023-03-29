s1={1,2,3,4}
s2={3,4,5,6,7}

s3= s1.union(s2) 
print(s3)

s3 = s1.intersection(s2)
print(s3)

# s1.intersection_update(s2)
# print(s1)

s3 = s1.difference(s2)
print(s3)

s3 = s2.difference(s1)
print(s3)

# s1.difference_update(s2)
# print(s1)

s3 = s1.symmetric_difference(s2)
print(s3)

# s1.symmetric_difference_update(s2)
# print(s1)
print("-------------------------------------------------------------------")
print(s1)
print(s2)
s4={8,9,7}
s5={2,3}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s4))
print(s5.issubset(s1))
print(s1.issuperset(s5))