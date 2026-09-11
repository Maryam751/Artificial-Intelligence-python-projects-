List1 = [10,20,30,40]
List2 = [50,30,70,80]

t = int(input("Enter a number "))
for i in range(len(List1)):
    for j in range(len(List2)):
        if List1[i] == List2[j]:
            print('true')
            break
    else:
        continue
    break    

else:
    print('false')    

    
