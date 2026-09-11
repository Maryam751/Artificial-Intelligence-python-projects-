A= [10,20,30,40]   
t = int(input("Enter a number: "))

for i in range(len(A)):
    if A[i] == t:
        print('true')
        break
else:
    print('false')















'''
    A= [10,20,30,40]   
t = int(input("Enter a number "))
search = False
for i in range(len(A)):
    if A[i] == t:
        search = True
        break

if search:
    print(" number is in the list A ")    
else:
    print(" number is not in the lisst A")    
    '''