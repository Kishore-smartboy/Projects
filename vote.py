import  math
a=int(input("enter the number  "))
z=1
for i in range(a):
   i=i+1
   z=z*i
print("the fact is ",z)
k=int(input("enter 0 to continue 1 to exit  ")) 
while(k==0):
    for i in range(a):
       a=int(input("enter the number  "))
       i=i+1
       z=z*i
    print("the fact is ",z)
    k=int(input("enter 0 to continue 1 to exit  ")) 



 