
#Task 1
#write a program to find those number which is divisible by 7 and multiple by 5,between 1500 abd 2700.
for i in range(1500,2700):
    if i % 7 == 0 and i % 5 == 0:
        print(i)





#Task 2
#Write a Python program to convert temperatures to and from Celsius, Fahrenheit. [Formula: c/5 = f-32/9 [ where c = temperature in Celsius and f = temperature in Fahrenheit]
#Expected Output:
#600C is 140 in Fahrenheit 450F is 7 in Celsius


c= float(input("enter value of temperature in celsius : "))
f = (c*9/5) +32
print(c , "C is " , int(f) , "in Fahrenheit : ")

f  = float(input("Enter temperature in Farenheit :"))
c = (f-32) *5/9
print(f," f is " , int(c) , "in celsius")




#Task 3
#Write a Python program to guess a number between 1 to 9.
#Note: User is prompted to enter a guess. If the user guesses wrong then the prompt
#appears again until the guess is correct, on successful guess, user will get a "Well
#guessed!" message, and the program will exit

'''
import random
number = random.randint(1, 9)
while True:
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == number:
        print("Well guessed!")
        break
    else:
        print("Wrong guess. Try again.")

'''
        


#Task 4   print asterik
for i in range(1, 6 ):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


    



#Task 5
#Write a Python program that accepts a word from the user and reverse it.
word = input("Enter a word: ")
reverse = word[::-1]
print("Reverse word:", reverse)




    

#Task 6
#Write a Python program to count the number Of even and Odd numbers from a
#series of numbers.
#Sample numbers : numbers (1, 2, 3, 4, 5, 6, 7, 8, 9)
#Expected Output :
#Number Of even numbers : 5 Number Of odd numbers : 4
Numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
even = 0
odd = 0
for num in Numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Number of even numbers:", even)
print("Number of odd numbers:", odd)


#Task 7
# Write a Python program that prints each item and its corresponding type from the following list.
#Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (O, -1), [5, 12],


Datalist = [ 1122, 21.56, 1+2j, True, 'Maryam',
            (0, -9), [20, 40, 60 ], 
            {"class": 'pyhton', "section": 'IT'}
            ]

for item in Datalist:
    print(item, type(item))



