'''
while condition:
    // block of code
    inc/dec


'''

# i=1
# while i<=5:
#     print("Royal")
#     # i+=1
#     i=i+1

# j=10
# while j<=20:
#     print(j ,end=" ")
#     j+=1

# for i in range(1,6):
#     print(i,end=" ")
# else:
#     print("Thank you")


# for i in range(1,6):
#     if i==4:
#         break
#     print(i,end=" ")
# else:
#     print("Thank You")

# j=1
# while j<=5:
#     if j==3:
#         break
#     print(j,end=" ")
#     j+=1
# else:
#     print("All Printed")

'''

1. Take one number from user and print multiplication table of that number.

n - 6
6 * 1 = 6
6 * 2 = 6
.
.
6 * 10 =60

2. print sum of 1 to 100 number.

3. find factorial of a number.

    5 - 120
    4 - 24

4. Take one number from user and find first and last digit of number.

n= 46373457

first digit : 4
last digit : 7

5. Take one number from user and sum of all digit.

n = 51321
sum = 5+1+3+2+1 = 12

6. Take one number from user and reverse that number.

n = 26464
output: 46462

7. check number is palindrom or not ?

n - 5252 (not)
n - 2662 - (yes)

8. Take one number from user and print in words.

n - 245

two four five

n - 11679

one one six seven nine

9. Take one number from user and count number of digit.

n= 56465

digit: 5

10. Check number is armstrong or not.

123
len=3
1^3 + 2^3 + 3^3 = 1+8+27 = 36
123!=36 -> not Armstrong

153
len=3
1^3 + 5^3 + 3^3 = 153
153=153 -> Armstrong


1634
len = 4
1^4 + 6^4 + 3^4 + 4^4 = 4+1296 + 81 + 256 = 1634
-> Armstrong


11. Take one number from user and check number is prime or not ?

    4 - not prime
    3 - prime

12. Print all the factor of number.

    12 - 1 2 3 4 6 12
    6 - 1 2 3 6

13. Check number is perfect number or not ?

    6 - 1 2 3 6 (1+2+3 = 6) -> perfect Number
    28 - 1 2 4 7 14 28 (1+2+4+7+14 = 28) -> perfect number

14. find GCD(HCF) of two Number.

    12 - 1 2 3 4 6 12
    6 - 1 2 3 6

    24 - 1 2 3 4  6 8 12 24 
    36 - 1 2 3 4 6 9 12 18 36

    hcf = 6

15. find LCM of two number.

    6 - 6 12 18 24 ...
    12 - 12 24 36..

    lcm = 12

    3  - 3 6 9 12 ... 
    4  -  4 8 12 ..

    lcm=12

    5 - 5 10 15 20 25 30 35  40 45..
    7 - 7 14 21 28 35 42..

    lcm = 35


'''
# print("-------")
# print(pow(2,4))
# print(pow(3,6))

# HCF
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# hcf=0

# if a<b:
#     min=a
# else:
#     min=b

# i=1
# while i<=min:

#     if a%i==0 and b%i==0:
#         hcf=i
#     i+=1

# print("Hcf is: ",hcf)

# LCM

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

if a<b:
    max=b
else:
    max=a

count=0
i=max
while True:
    if i%a==0 and i%b==0:
        lcm=i
        break
    i+=max
    count+=1

print(lcm)
print(count)