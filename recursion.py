#  10 to 1 using recursion.

# def printNum(n):
    
#     if n==1:
#         print(n)
#         return
    
#     print(n)
#     printNum(n-1)


# printNum(10)

# Factorial

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n-1)


# print(fact(6))

# 1 to 10 using recursion.

# def printNum(n):
    
#     if n==1:
#         print(n)
#         return
    
#     printNum(n-1)
#     print(n)
    
# printNum(10)

# Print Fibonacci series...
#  0 1 1 2 3 5 8 13 ....

# def fib(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1

#     return fib(n-1)+fib(n-2)

# n=10
# for i in range(1,n+1):
#     print(fib(i))

def fibonacci(n,first, second):

    if(n==0):
        return

    print(first,end=" ")
    fibonacci(n-1,second,first+second)


fibonacci(10,0,1)



