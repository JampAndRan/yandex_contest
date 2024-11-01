def makeprefixsum(list_numbers):
    prefixsum=[0]*(len(list_numbers)+1)
    for i in range(1,len(list_numbers)+1):
        prefixsum[i]=prefixsum[i-1]+list_numbers[i-1]
    return prefixsum


def cars(new_num, k):
    count_k=0
    last=1
    for first in range(len(new_num)):
        while last<len(new_num) and new_num[last]-new_num[first]<=k:
            if new_num[last]-new_num[first]==k:
                count_k+=1
            last+=1
    return count_k


n,k= map(int,input().split())
list_numbers=[int (i) for i in input().split()]
new_num=makeprefixsum(list_numbers)
count=cars(new_num,k)
print(count)
