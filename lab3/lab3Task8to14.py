#Task 8
#Write a Python program that prints all the numbers from O to 6 except 3 and 6.
#Note : Use 'continue' statement

for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i , end=" ")

#Task 9
# fabonanci series
a = 0
b = 1
while a <= 50:
    print(a, end=" ")
    a , b = b, a+b 



#Task 9
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#Task 10
# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

array = []
for i in range(m):
    row = []    
    for j in range(n):
        row.append(i * j)
    array.append(row)

print(array)         





#Task 11
# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case)
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line.lower())

for line in lines:
    print(line)



#Task 12
# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a
# comma separated sequence. Sample Data 0100,0011,1010,1001,1100,1001 : Expected Output : 1010   
numbers = input("Enter binary numbers: ").split(",")
result = []
for num in numbers:
    decimal = int(num, 2)

    if decimal % 5 == 0:
        result.append(num)

print(",".join(result))   


#Task 13
#Write a Python program that accepts a string and calculate the number of digits and letters.
#Sample Data : Python 3.2 Expected Output :
#Letters 6
#Digits 2

text = input("Enter a string ")
letters = 0
digits = 0
for char in text:
    if char.isalpha():
        letters +=1
    elif char.isdigit():
        digits+=1
print("Letters " , letters)            
print("Digits " , digits)            





#Task 14
 #Write a Python program to check the validity of password input by users. Validation
#At least 1 letter between (a-zl and 1 letter between (A-ZI.
#At least 1 number between [0-91.
#At least I character from
#Minimum length 6 characters.
#Maximum length 16 characters

password = input("Enter password: ")

has_lower = False
has_upper = False
has_digit = False
has_special = False
special_chars = "$#@!%^&*?"

# Check length first
if 6 <= len(password) <= 16:
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    # Verify all conditions are met
    if has_lower and has_upper and has_digit and has_special:
        print("Valid Password!")
    else:
        print("Invalid Password: Missing required character types.")
else:
    print("Invalid Password: Length must be between 6 and 16 characters.")