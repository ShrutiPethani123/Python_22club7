'''

1. Take one string from user and make string using first , middle and last character.

    str= "Pakistan"
    output: Pin

2. Create a string made of the middle three characters.if string length have even length than print invalid input.

    str="javapython1"
    op:pyt

3. Count number of Alphabats , digit and special character from string.

    str:"tyi244vj^*gj"

    o/p:
    digit:3
    alpha: 7
    special charcters: 2

4. Take two string from user and merge that two string using following rules:

    1. There are two string s1 and s2 with same length.
    2. s1 = ABC , s2=PQR
    3. output: APBQCR

5. Add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
    
Example:

    abcd - abcding
    string - stringly
    am - am
    ing - ingly
    
  
6. Remove the nth index character from a string

    str - India
    n - 3 (remove i )
    o/p - Inda


7. Change a given string to a new string where the first and last chars have been exchanged

    str - wxyz
    o/p - zxyw

8. Remove the characters which have odd index values of a given string

    str: Python
    o/p :  pto

9. Get the last part of a string before a specified character

    exa: https://www.python.org/downloads
    o/p : downloads

10. Reverse a string if it's length is a multiple of 4.

    str- abcd
    o/p: dcba

    str - python
    o/p - python

11. Convert a string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters


    str- PyThon
    o/p- PYTHON

    str- TeachING
    o/p - TeachING

12.  Print the following floating numbers upto 2 decimal places

    a=12.99856
    o/p:13.00

    a=45.231547
    o/p:45.23


13. Reverse a string.

    s=python
    o/p: nohtyp


    
14. Reverse words in a string

    s= India is best country
    o/p: country best is India

    
15. Compute sum of digits of a given string

    s=abcd1234
    ans: 10
    
'''

# 1.



# str=input("Enter a string: ")

# first=str[0]
# last=str[len(str)-1]
# middle=str[(len(str)-1)//2]

# op = first + middle + last

# print(op)

# 2.

# str=input("Enter a string: ")

# if(len(str)%2==0):
#     print("Invalid Input!!")
# else:
#     m=len(str)//2
#     s = str[m-1:m+2]
#     print(s)


# python(6) - invalid
# javam(5) - ava


# 3.

# str=input("Enter a string: ")

# for i in str:
#     print(i)

# for i in range(0,len(str)):
#     print(i)

# alpha=0
# num=0
# symbol=0
# for i in str:

#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         num+=1
#     else:
#         symbol+=1

# print("Alphabets: ",alpha)
# print("Numbers: ",num)
# print("Special charcaters: ",symbol)

# 6.

# Nihar -> Niar
# 01234
# -5 -4 -3 -2 -1
# str=input("Enter a string: ")
# i = int(input("Enter index: "))

# # if i<len(str) and abs(i)<=len(str):
# if i>=(-len(str)) and i<len(str):
#     new = str[:i] + str[i+1:] #
#     print(new)
# else:
#     print("Invalid Input!!")

11.
s= input("Enter a string: ")
count=0
for i in s[:4]:
    if i.isupper():
        count+=1

if(count>=2):
    s=s.upper()

print(s)


