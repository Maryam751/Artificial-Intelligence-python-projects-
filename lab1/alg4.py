List1 = [1,2,3,4,5,6]
for i in range(len(List1)):
    for j in range(i+1 ,len(List1)):
        if List1[i] == List1[j]:
            print("Duplicate Found")
            break
    else:
        continue
    break    
else:
    print("Duplicate not found")    