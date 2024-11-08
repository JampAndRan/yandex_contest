n,b=map(int,input().split())
list_a=[int(i) for i in input().split()]
count=0
ost=0
for i in range (n):
    ost+=list_a[i]
    if ost>=b:
        count += ost
        ost-=b
    else:
        count += ost
        ost=0
count+=ost
print(count)
