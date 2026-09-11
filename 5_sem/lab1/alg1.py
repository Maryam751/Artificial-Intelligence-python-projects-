A= [10,20,30,40]   
t = int(input("Enter a number: "))

for i in range(len(A)):
    if A[i] == t:
        print('true')
        break
else:
    print('false')

