'''
dictionary:

key:value

'''

d1 = {

    12: 'lamya',
    23: 'nihar',
    35: 'khush',
    12: 'jiya'
}


print(d1)
print(d1[12])
print(type(d1))
print("length: ",len(d1))

d2={
    'birthdate':'23march2000',
    'age':22,
    'isActive':True,
    'colors':['red','green','blue']

}

print(d2['age'])
print(d2['colors'][2])

d3 =dict(name='lamya' , age='17',city='ahm')
print(d3)

# access the value

print(d3['name'])
# print(d3['name123']) #error
print(d3.get('name')) # value
print(d3.get('name1312')) # None


print(d2.keys())
print(d2.values())
print(d2.items())

d2['isActive']=False
print(d2)

d2.update({'age':24})
print(d2)

d2.update({'year':2022})
print(d2)

d2['name']="khush"
print(d2)

d2.pop('name')
print(d2)

d2.popitem()
print(d2)
d2.popitem()
print(d2)

# del d2
# print(d2)

del d2['age']
print(d2)

d2.clear()
print(d2)

