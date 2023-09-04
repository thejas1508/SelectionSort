#SELECTION SORT
#FINDING THE LARGEST NUMBER IN LIST
listlen=int(input("Enter the List Size:"))
alist=[]
maximum=0
count=0
#Loop
while (count<listlen):
    num=int(input("Enter a Number:"))
    alist.append(num)
    count=count+1
#Displaying List
#print(alist)
#DECREMENT THE ORDER
for i in range(1,listlen-1):
    numbers=list[i]
    print(numbers)
    change=i-1
#REPLACEING THE ORDER     
    while change>=0:
        if numbers<alist[change]:
            alist[change+1]=alist[change]
            change=change-1
            alist[change+1]=numbers
        else:
            break
#DISPLAY THE OUTPUT        
    print(alist)    
       
            

