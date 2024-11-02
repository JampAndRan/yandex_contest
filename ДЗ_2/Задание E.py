n=int(input())
list1=[int(i) for i in input().split()]
list1.sort()
if n%2==1:
    l=n//2-1
    r=n//2
else:
    l=(n-1)//2
    r=n//2
for j in range(n):
    if (n-j)%2==1:
        if j==n-1:
            print(list1[r])
        else:
            print(list1[r], end=" ")
        r+=1
    else:
        print(list1[l], end=" ")
        l-=1
