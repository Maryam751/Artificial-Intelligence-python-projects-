#while loop

count = 0
while(count<10):
    count =count+1
    print("Maryam")


#single statement


counter = 0
#while(counter ==0) : print("hiiiiiiii") 



#for loop
#example 1
print("List Iteration ")
list = ["geeks ","for ","geeks"]
for i in list:
    print(i)


#example2
print("\nTuple iteration ")
t = ("geeks ","for ","geeks")
for i in t:
    print(i)


#example 3
print("\nString iteration ")
s = "geeks"
for i in s:
    print(i)




#Iteration  by index
l1 = ["geeks ","for ","geeks"]
for index in range(len(list)):
    print(list[index])



#loop control statement
#print all letter except e and s
for letter in 'geeksforgeeks':
    if letter =='e' or letter =='s':
        continue
    print("current letter :" ,letter )



#break statement
#break loop asa it sees e or s
print("print with break statement")
for le in 'geeksforgeeks':
    if le == 'e' or le == 's':
        break
    print("current letter : ",le)



#function
def myfunction():
    print("Hello from my function")

#function calling
myfunction()




#parameters
def ourfunc(fname):
    print(fname + " Refsnes")

#function calling
ourfunc("Email")
ourfunc("Tobias")
ourfunc("Linux")


#default parameter
def myfunc(country = "Noorway"):print(" i am from "+country)

myfunc("Pakistan")
myfunc()
myfunc("USA")
myfunc("UK")


def fruit(food):
    for x in food:
        print(x)


fruits = ["banana", "apple ","peach" , "strawberry"]
fruit(fruits)       



#return values
def retfunc(x):
    return 5*x


print(retfunc(5))
print(retfunc(7))
print(retfunc(8))
print(retfunc(9))




#Keyword argument
def mfunction(child1,child2,child3):
    print("youngest child is  " +child3)


mfunction(child1="zain",child2="ali",child3="furqan")



#Python clases
class Myclass:
    x=1

c1 = Myclass()
print(c1.x)    



#init function

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


      

P1 = Person('Maryam',21)
print(P1.name)
print(P1.age)


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print("My name is "+self.name)  

S1=Student("Maryam",21)
S1.show()

