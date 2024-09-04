def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:            
            return i
    return -1
arr=list(map(int,input("Enter the elements to sort: ").split()))
target=int(input("Enter element to search: "))
result=linear_search(arr,target)
if result!=-1:    
    print(f"Found at index {result}")
else:    
    print("Not Found")
                       
