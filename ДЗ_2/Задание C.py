def masha(new_num, r):
    count=0
    last=1
    for first in range(len(new_num)):
        while last<len(new_num) and new_num[last]-new_num[first]<=r:
            last+=1
        count+=len(new_num)-last
    return count


n,r= map(int,input().split())
list_numbers=[int (i) for i in input().split()]
count=masha(list_numbers,r)
print(count)
