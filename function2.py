def display(name , age):
    print(name, " ", age )

display("lamya",20)

# Arbitary argument: *args

def printMarks(*mark):
    print(mark , type(mark))
    print(mark[2])

printMarks(90,34,67)

# Keyword Arguments

def fun1(name1 , name2 , name3):
    print(name1, name2,name3)

# fun1('nihar','lamya','khush')
fun1(name1='khush' ,name3='lamya', name2='nihar')


# default perameter


# def fun2(name , city="ahmedabad"):
#     print(name , city)

# def fun2(batch=35, name , city="ahmedabad"): - invalid non-default argument follows default argument
def fun2(name , batch=35 , city="ahm"):
    print(name ,  batch , city)


fun2('raj')
fun2('siya','baroda')
fun2('siya',city='baroda')



# Arbitary keyword Arguments (**kwargs)

def fun3(**name):
    print(name['fname'],name['lname'],name['add'])
    print(name , type(name))

fun3(add='india',fname="raj" , lname='patel')

def printMarks(name , *mark ):
    print(mark , type(mark), name)
    print(mark[2])

printMarks(90,34,67,"raj")

def printMarks(*mark, **name ):
    print(mark , type(mark), name)
    print(mark[2])

# printMarks(90,34,67,"raj" , n1="1",n2=3 ,45,67) - invalid
printMarks(90,34,67,"raj" , n1="1",n2=3 )

def printMarks(name1,*mark,add="ahm" ,**name ):
    # print(mark , type(mark), name , add)
    # print(mark[2])
    print(name1 , add , mark , name)

# printMarks(90,34,67,"raj" , n1="1",n2=3 ,45,67) - invalid
# printMarks(90,34,67,"raj" , n1="1",n2=3 )
printMarks('khush','baroda',45,67,89 ,fname='khush',lname='amin')
printMarks("khush",23,45,67,fname='khush',lname='amin')
printMarks("khush",23,45,67,fname='khush',lname='amin' , add="baroda",age=45)
printMarks("khush", mark=(23,45,67),fname='khush',lname='amin')


def printMarks2(name1, add="ahm", *mark ,**name ):
    # print(mark , type(mark), name , add)
    # print(mark[2])
    print(name1 , add , mark , name)
printMarks2("khush", "baroda",23,45,67,fname='khush',lname='amin' ,age=45)
# printMarks2("khush", add="baroda",23,45,67 ,fname='khush',lname='amin' ,age=45)  #positional argument follows keyword argument



def fun3(name, age=34 ):
    print(age)

fun3(36)
# fun3(age=45 ,"raj") #positional argument follows keyword argument