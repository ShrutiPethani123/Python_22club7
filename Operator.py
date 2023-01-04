"""
a+b

operands -> a , b
operator -> +

1. Arithmetic Operator ( +   -  *  /  %  //  **)
2. Logical Operator (and, or, not)
3. Relational/Conditional  Operator (< > <= >= == != )
4. Assignment Operator (=  += -= *= /= ....)
5. Bitwise Operator (& | ~  ^ << >>)
6. Membership Operator
7. Idntity Operator


// ++ , -- inc/ dec operator are not there.


"""
# 1. Arithmetic Operator ( +   -  *  /  %  //  **)

# a=int(input("Enter no: "))
# b=int(input("Enter no: "))

# # print("Additon of ",a," and ", b , " is ", a+b)
# print(f"Addition of {a} and {b} is {a+b}")
# print(f"Substraction of {a} and {b} is {a-b}")
# print(f"Multiplication of {a} and {b} is {a*b}")
# print(f"Division of {a} and {b} is {a/b}")
# print(f"Floor Division of {a} and {b} is {a//b}")
# print(f"Modulus of {a} and {b} is {a%b}")
# print(f"Exponant of {a} and {b} is {a**b}")


"""
2. Logical Operator (and, or, not)

and - To login time should write both username and password right

A   B   A and B

F   F   F
F   T   F
T   F   F
T   T   T

or - signup using  Google , Facebook , Linkdin

A   B   A or B

F   F   F
F   T   T
T   F   T
T   T   T

not - Turn Light ON/OFF

A   not A

T   F
F   T


"""
# a=float(input("Enter no: "))
# b=float(input("Enter no: "))
# c=float(input("Enter no: "))

# print(a>b and b<c)  #3>2 and 2<1 => T and  F => F
# print(True and False)
# print(True and True)
# print(False and True)

# a=3 ,b=2 , c=1
# print(a>b or b>a)  
# print(a>b and b>a)
# print(b<c or a>c) #F or T -> T

# print(not a>b)
# print(not False)
# print(not True)
# print(not 56)
# print(not 0)
# print(not -1)

# Logical Operator only work on Boolean type


# 3. Relational Operator (< > <= >= == != )
#  -> It will return True or False

# a=float(input("Enter no: "))
# b=float(input("Enter no: "))

# print(a>b)
# print(a<b)
# print(a<=b)
# print(a==b)
# print(a!=b)


# 4. Assignment Operator (=  += -= *= /= ....)

# a=6
# # a=a+2
# a+=2

# #  a+=n  <=>  a=a+n

# b=5
# b-=8

# print(a)
# print(b)

# ++ , -- -> not available in python
# a++ -> a+=1 -> a=a+1

"""

5. Bitwise Operator (& | ~  ^ << >>)

& 

A   B   A & B

0   0   0
0   1   0
1   0   0
1   1   1

| 

A   B   A | B

0   0   0
0   1   1
1   0   1
1   1   1

^ 
A   B   A & B

0   0   0
0   1   1
1   0   1
1   1   0

12 - 1100
34 - 0010 0010

128    64    32    16      8    4    2    1

56 - 0011 1000
50 - 0011 0010
20 - 0001 0100

1111 - 15
1100 - 12
1100 1101 - 205
1111 0011 - 243

14 & 18

14 - 0000 1110
     &&&& &&&&
18 - 0001 0010
 ---------------
     0000 0010 (2)

14 - 0000 1110
     |||| ||||
18 - 0001 0010
----------------
     0001 1110 (30)

14 - 0000 1110
     ^^^^ ^^^^
18 - 0001 0010
-----------------
     0001 1100 ()


13    - 0000 1101 (13)
13<<1 - 0001 1010 (26)
13<<2 - 0011 0100 (52)

(n<<m) -> n*2^m


13    -  0000 1101 (13)
13>>1 -  0000 0110 (6)
13>>2 -  0000 0011 (3)
13>>3 -  0000 0001 (1)
13>>4 -  0000 0000 (0)

(n>>m) -> n/(2^m)

"""

print(14 & 18)
print(14 | 18)
print(14 ^ 18)
print(13<<1)  
print(13<<2) #13*2^2 = 52
print(13>>1)
print(13>>3)
print(13>>4)
print(13>>28)




