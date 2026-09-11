
#simple print statemant
print("Hello World")


#comments
x=1
# the value of x is 1
if(x>0):
    print("comment begin with hash sign # ")


#getting input
text = input("enter the value ")   

print(text)

#multiple statement
print("Statement 1")
print("Statement 2")

#we can write multiple in following way
print("staemant 1") ; print("statement 2")


#indentation

y=1
#if y>0:
#print("This statement has no indentation")
#print("This statement has no indentation")


#single space indentation
z=1
if z>0:
 print("This statement has indentation")
 print("This statement has indentation")

#single tab indentation
u=1
if u>0:
    print("This statement has indentation")
    print("This statement has indentation")

'''

#datatypes 
a= 1452
print(type(a))

b= (-543)
print(type(b))

c= 0
print(type(c))

d= 1.098
print(type(d))

e= (-1.098)
print(type(e))

f= .098
print(type(f))

g= 1.21e-10
print(type(g))

h= 5E220
print(type(h))




#real and imaginary
i = complex(1,2)
print(type(i))
print(i)

k = 1+2j
print(type(k))
print(k)

l = 1+2J
print(type(l))
print(l)



#bool expression
m= True
print(type(m))

n= True
print(type(n))


#strings
str1 = "String"
print(str1)

str2 = 'String'
print(str2)

#str3 = "String'
#print(str3) # it represent error bcz string start with double quote and end with single quote


#str4 = 'String" 
#print(str4) # it represent error bcz string start with single quote and end with double quote

str5 = "day's" 
print(str5)

str6 = 'day"s'
print(str6)



#escape sequence
print("This is a blackslash mark (\\) ")
print("This is a  tab \t  key   ")
print("This is a \'single quote\'")
print("This is a \"double quote \" ")
print("This is a newline \n newline ")



#accessing string element
str = "python tutorial"
print(str[0])
print(str[-15])
print(str[14])
print(str[-1])
print(str[4])
print(str[-11])
#print(str[16]) # out of index range it represnt eror




#creating list 
list1 = [1,12,14,16,2]   # list have integer values
print(list1)

list2 =['red' , 'blue' , 'pink' , 'yellow']
print(list2)
print(list2[2]) 

list3 = ['red ' ,2, 4, 7.5 , 'pink'] #list contain  integer float and stringvalue
print(list3)

list4 = []
print(list4)


#accessing element of list 


colors =['red' , 'blue' , 'pink' , 'yellow', 'black' , 'orange']
print(colors)
print(colors[1]) 
print(colors[2] , colors[3]) 
print(colors[3]) 
print(colors[4]) 
print(colors[5]) 
print(colors[-1]) 


#list slicing

print(colors[0:2])
print(colors[1:2])
print(colors[1:-3])
print(colors[1:])
print(colors[:3])
print(colors[:])


'''