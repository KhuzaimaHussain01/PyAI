n=[10,20,30,40,50]
t=int(input("Enter the target number:"))
low=0
high=len(n)-1
while low<=high:
    mid=(low+high)//2
    if n[mid]==t:
        print("Target number found at index:",mid)
        break
    elif n[mid]<t:
        low=mid+1
    else:
        high=mid-1
else:
    print("Target number not found in the list")