n=int(input())
l=[]
sum=0
for i in range(n):
    a=int(input())
    l.append(a)
l.sort()
n=int(input())
z=len(l)
m=len(l)
z=1
for i in range(n):
    sum=sum+(l[m-z])
    print(l[m-z])
    z=z+1
print(sum)
