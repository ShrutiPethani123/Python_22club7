# 1. Take one number from user and check number is positive or negative

# a=int(input("Enter a no: "))

# if a>0:
#     print(f"{a} is positive")
# elif a==0:
#     print(a,"is Zero")
# else:
#     print(f"{a} is Negative")

# print('Thank you!!')


"""
1. Take one number from user and check number is positive or negative
2. Take one number from user and check number is odd or even.
3. take two number from user and find minimum number of them.
4. take Three number from user and find maximum number of them.
5. Take one number from user and check number is divisible by 7 or not.
6. check the candidate is eligible for vote or not.
7. Take cost price and selling price from user and find profit or loss.

        cp-100
        sp- 500

        profit -> 400

8. Take one number from user and print week days according to that number.
    1 - Sunday
    2 - Monday
    .
    .
    7 - Satuarday
    
    other input: Invalid 

9. Write  a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer, 
    calculate percentage and grade according to given conditions:

	If percentage >= 90% : Grade A
	If percentage >= 80% : Grade B
	If percentage >= 70% : Grade C
	If percentage >= 60% : Grade D
	If percentage >= 40% : Grade E
	If percentage < 40% : Grade F

10. Count Total number of notes.

    n = 1863

    2000 - 0 
    500 - 3
    200 - 1
    100 - 1
    50 - 1
    10 - 1
    5  - 0
    1 - 3

    n2000 = n//2000
    n=n%2000
    n500 = n//500
    n=n%500

11. Write a program to take input from user in seconds and convert into hours and minutes.

	10000 - 2 :46 : 40

12. Write a program to accept the cost price of car display the road tax to be paid 
    according to the following criteria:

    cost price (in Rs)       Tax
    >100000                  15%
    >50000and <=100000        10%
    <=50000                   5% 

13. Write a program to input electricity unit charge and calculate the total 
	electricity bill according to the given condition:

	For first 50 units Rs. 0.50/unit
	For next 100 units Rs. 0.75/unit
	For next 100 units Rs. 1.20/unit
	For unit above 250 Rs. 1.50/unit

	300 
	50 - 0.50 = 25
	100 - 0.75=75
	100 - 1.20 = 120
	50 - 1.50  = 75   total - 295

    130

    50 - 0.50= 25
    80 - 0.75 = 60

    total = 85


"""

# Nested if


# n=int(input("Enter a no:"))

# if n>0:
#     # pass
#     if n>10:
#         print(n , "is greater than 10")
#     else:
#         print(n , "is less than 10")
    
# elif n==0:
#     print("Zero")
# else:
#     print("Negative")

#shorthand Notation for if

age=int(input("Enter age:"))
if age>18:print("Eligible for vote");print("Bye");print("hyy");
else:
    print("else")

#shorthand Notation for if else
age=int(input("Enter age:"))
print("Eligible for vote");print("Bye")if age<=18 else print("Not Eligible for vote");print("xyz");print("If") if age>50 else print("else")