n, k=map(int,input().split())
list_num=[int(i) for i in input().split()]
new_num=sorted(list_num)

def cars(new_num, k):
    if len(new_num)==1:
        return 1
    else:
        max_count=0
        count = 1
        last=1
        for first in range(len(new_num)):
            while last<len(new_num) and new_num[last]-new_num[first]<=k:
                count+=1
                if count>=max_count:
                    max_count=count
                last+=1
            count-=1
        return max_count

max_count=cars(new_num,k)
print(max_count)

