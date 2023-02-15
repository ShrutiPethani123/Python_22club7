# Alignment related methods
# str='India is best country!! and pakistan is worst country'
'''
print(str)
print(str.center(100))
print(str.center(100,'😢'))
print('😢🤣😊')
print(str.ljust(50,'🤷'))
print(str.rjust(50,'🤷'))
'''


# count method

'''
print(str)
print(str.count('i'))
print(str.count('st'))
print(str.count('nt'))
print(str.count('country'))
print(str.count('country',25))
print(str.count('country',25,100))

'''
# print(str.encode())
# print(str.encode('utf16'))

'''
print(str.endswith('y'))
print(str.endswith('try'))
print(str.endswith('try',10,21))
print(str.startswith('ind'))
print(str.startswith('!',21))
print(str.startswith('!!',21,40))

'''

# expandtabs

'''
print("rollNo\t".expandtabs(20) + "Name\t".expandtabs(25) + "Marks1\tMarks2")
print("101\t".expandtabs(20) + "Nihar\t".expandtabs(25) + "94\t97")
print("102\t".expandtabs(20) + "Khush\t".expandtabs(25) + "94\t97")

'''

# print("java\tpython")
# print("Pythonjava654646\tjava")

str='India is best country!! and pakistan is worst country'

print(str.find('i'))
print(str.find('best'))
print(str.find('is',25))
print(str.find('i',25,40))
print('----------------------')

print(str.index('i'))
print(str.index('best'))
print(str.index('is',25))
print(str.index('i',25,40))

print("------------------")

# print(str.find('z')) # if string not present than return -1
# print(str.index('z')) # if string not present than return error

print(str.rfind('try'))
print(str.rfind('try',30))
print(str.rfind('India',30))
print(str.rfind('try',-2))
print(str.rindex('try'))






