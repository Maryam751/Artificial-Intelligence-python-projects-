array = [6,38,9,51,20,55,27,30,61,50,90]
array.sort()
print("Sorted array " , array)
low = 0
high = len(array)-1
search = int(input("Enter number to search : "))
while (low <= high):
    mid = (low+high)//2
    print("lowest index is : ",low ,"mid index number is : ",mid ,"highest number index is : ",high)
    if array[mid] == search:
        print("Successfully found the number : ",search ,"At index : ",mid)
        break
    elif array[mid] < search :
        low = mid + 1
    else:
        high = mid-1
else:
    print("Invalid number to search")