s1="Nihar and khush"
s2=' is good boys'

# print(s1+s2)
# print(s1.__add__(s2))

# s1=4
# s2=5
# print(s1+s2)
# print(s1.__add__(s2))

# s1=4
# s2='java'
# s2='5'
# print(s1+s2) - invalid for different data type of s1 and s2
# print(s1.__add__(s2)) - invalid for different data type of s1 and s2

# s1=4.5
# s2=7
# print(s1+s2)
# print(s1.__add__(s2))

# print(s1,s2)
# print("Length of string 1: ",len(s1))
# print("length of string 2: ",len(s2))

# print(len(s1+s2))

s='india is Best!! Today is FRIDAY'
print(id(s))
# print(s.capitalize())
s2=s.capitalize()
print(s)

print("Location of s: ",id(s))
print("Location of s2: ",id(s2))

# s=s.capitalize()
# print("Location of s: ",id(s))

s3=s.capitalize()
print("Location of s: ",id(s3))

print("Capitalized:- ",s.capitalize())
print("Upper:- ",s.upper())
print("Title:- ",s.title())
print("Lower:- ",s.lower())
print("Swapcase:- ",s.swapcase())
print("caseFold:- ",s.casefold())

'''
string is immutable

'''

s="German eszett, see ß."
print(s.lower())
print(s.casefold())