'''
function: 

Types:

1. buit in (pre define) Function
2. user define functions (UDF)

'''

def display():
    print("Hello")

def add(a,b):
    return a+b

display()
ans = add(4,8)
print(ans)


def isPrime(n):
    i=2
    while i<n:
        if n%i==0:
            return False
        i+=1
    return True

if(isPrime(50)):
    print("Prime Number")
else:
    print("Not Prime")


'''
1. Take one number from user and check that number if prime or not using function.
2. Take one number from user and return reverse number of that number.
3. Take one number from user and check that number if perfect number.

6 : 1 2 3 6 (1+2+3 = 6), 28

4. Take two number form user and find hcf(GCD) of that two number.

6: 1 2 3 6
12: 1 2 3 4 6 12

gcd: 6

15: 1 3 5 15
25: 1 5 25

gcd:5

5. Take two number form user and find hcf(GCD) of that two number.

12: 12 24 36 48
6: 6 12 18

lcm:12

3: 3 6 9 12 15
4: 4 8 12 16
lcm: 12

'''
