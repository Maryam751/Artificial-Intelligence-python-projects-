List1 = [10,20,30,40]
List2 = [50,60,70,80]

t = int(input("Enter a number "))
for i in range(len(List1)):
    if List1[i] == t:
        print("True")
        break

else:
    for i in range(len(List2)):
        if List2[i] == t:
            print('True')
            break
        else:
            print('false')