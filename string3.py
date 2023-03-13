# Alignment related methods
str='India is best country!! and pakistan is worst country'


# print(str)
# print(str.center(100))
# print(str.center(100,'&'))
# print('😢🤣😊')
# print(str.ljust(100,'🤷'))
# print(str.rjust(100,'🤷'))




# count method


# print(str)
# print(str.count('i'))
# print(str.count('st'))
# print(str.count('nt'))
# print(str.count('country'))
# print(str.count('country',25))
# print(str.count('country',25,100))


# print(str.encode())
# print(str.encode('utf16'))


# print(str.endswith('y'))
# print(str.endswith('try'))
# print(str.endswith('try',10,21))
# print(str.startswith('ind'))
# print(str.startswith('!',21))
# print(str.startswith('!!',21,40))



# expandtabs


# print("rollNo\t".expandtabs(20) + "Name\t".expandtabs(25) + "Marks1")
# print("101\t".expandtabs(20) + "Nihar\t".expandtabs(25) + "94")
# print("102\t".expandtabs(20) + "Khush\t".expandtabs(25) + "94")



# print("java\tpython")
# print("Pythonjava654646\tjava")

str='India is best country!! and pakistan is worst country'

# print(str.find('i'))
# print(str.find('best'))
# print(str.find('is',25))
# print(str.find('i',25,40))
# print('----------------------')

# print(str.index('i'))
# print(str.index('best'))
# print(str.index('is',25))
# print(str.index('i',25,40))

# print("------------------")

# print(str.find('z')) # if string not present than return -1
# print(str.index('z')) # if string not present than return error

# print(str.rfind('try'))
# print(str.rfind('try',30))
# print(str.rfind('India',30))
# print(str.rfind('try',-4))

# print(str.rindex('try'))

print("---------------------")


# s="Java Is Best"
# s1="PYTHON"
# s2="php"
# print(s.isupper())
# print(s1.isupper())

# print(s.islower())
# print(s2.islower())

# print(s.title()) 
# print(s.istitle())  #only first letter of all word must be capital and all other must in small letter
# print(s1.istitle())


s = "12235352"
s2="NiharKhush"
s3="22club7dgsd"
s4="&^%HJGJGJ"

# print(s.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())
# print(s4.isalnum())

# print(s.isalpha())
# print(s2.isalpha())
# print(s3.isalpha())
# print(s4.isalpha())

# print(s.isdigit())
# print(s.isdecimal())
# print(s.isnumeric())

# s1 = "9876543210"
# # s1="352.34634" - false
# s2 = "5⁴"
# s3 = "②⓪②②"
# s4 = "½"
# s5 = "二千二十二"

# print(s1.isdigit())
# print(s2.isdigit())
# print(s3.isdigit())
# print(s4.isdigit())
# print(s5.isdigit())

# print()
# print(s1.isdecimal())
# print(s2.isdecimal())
# print(s3.isdecimal())
# print(s4.isdecimal())
# print(s5.isdecimal())

# print()
# print(s1.isnumeric())
# print(s2.isnumeric())
# print(s3.isnumeric())
# print(s4.isnumeric())
# print(s5.isnumeric())

# s="fhsdh" - valid
# s='233dg' 
# s="dfds45" - valid
# s='&asfsd'
# s="_arestg" - valid
# s="-werwet"
# s="class" - valid
# s="def" - valid
# print(s.isidentifier())

# s="345"
# s="dsgdf34534"
# s="46&^Ghgkh"
# print(s.isascii())
# print(s3.isascii())


s = " Python is Funny Language and Everyone Enjoy it"
# print(s.split())
# print(s.split('a'))
# print(s.split('E'))
# print(s.split('a',2))

# print(s.rsplit('a'))
# print(s.rsplit('a',2))

# list = s.split()
# print(list)
# print("-".join(list))

# str1="java python c++ python"
# str="**"
# print(str.join(str1))

# print(str1.partition("y"))
# print(str1.partition("th"))
# print(str1.rpartition("th"))


# a=str1.rpartition("th")
# print(type(a))
# print("-".join(a))


# s="&&&&&&&&&&&&#############Ni&har&&&&&&&&&&&&"
# print(s.lstrip("&"))
# print(s.rstrip("&"))
# print(s.strip("&#"))


s='khush'
print(s.zfill(8))
print(s.zfill(6))

dd = input("Enter date(DD):")
mm = input("Enter Month(MM):")
print(f"{dd.zfill(2)} / {mm.zfill(2)} / 2023")








