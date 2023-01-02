"""
a+b

operands -> a , b
operator -> +

1. Arithmetic Operator ( +   -  *  /  %  //  **)
2. Logical Operator
3. Relational Operator
4. Assignment Operator
5. Bitwise Operator
6. Membership Operator
7. Idntity Operator
8. Ternary Operator

// ++ , -- inc/ dec operator are not there.


"""
# 1. Arithmetic Operator ( +   -  *  /  %  //  **)

a=int(input("Enter no: "))
b=int(input("Enter no: "))

# print("Additon of ",a," and ", b , " is ", a+b)
print(f"Addition of {a} and {b} is {a+b}")
print(f"Substraction of {a} and {b} is {a-b}")
print(f"Multiplication of {a} and {b} is {a*b}")
print(f"Division of {a} and {b} is {a/b}")
print(f"Floor Division of {a} and {b} is {a//b}")
print(f"Modulus of {a} and {b} is {a%b}")
print(f"Exponant of {a} and {b} is {a**b}")
