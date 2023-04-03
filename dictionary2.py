d1={
    1:"ram",
    2:'shyam',
    3:"joy",
    4:'roy'
}
print(d1)

# for i in d1:
#     print(i,d1[i])

# for i in d1.items():
#     print(i)

# for i in d1.keys():
#     print(i)

# for i in d1.values():
#     print(i)


# d2 = d1.copy()
# print(d2)

# nested dictionary

royal= {
    's1':{
        'name':"Nihar",
        'age':50,
        'address':"ahm",
        'batch':'22club7'
    },
    's2':{
        'name':"Khush",
        'age':60,
        'address':"ahm",
        'batch':'22club7'
    },
    's3':{
        'name':"Lamya",
        'age':100,
        'address':"ahm",
        'batch':'22club7'
    }
    
}

# print(royal)

for i in royal['s1']:
    print(i,royal['s1'][i])

print(royal['s3']['name'])

a=('key1','key2','key3')
b=1
d3 = dict.fromkeys(a,b)
print(d3)

'''
1. Make 2 dictionary and merge that two dictionary.


2. Print sum of all values of dictionary.
3. count how many data available in dictionary.
4. Find Maximum and Minimum values in dictionary

'''

d1={
    1:10,
    2:20,
    3:30,
    4:40
}

max= d1.get(1)
min= d1.get(1)

for i in d1.values():
    if max<i:
        max=i

    if min>i:
        min=i

print(max ,min)

dict
