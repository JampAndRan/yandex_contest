def makeprefixsum(list_numbers):
    prefixsum=[0]*(len(list_numbers)+1)
    for i in range(1,len(list_numbers)+1):
        prefixsum[i]=prefixsum[i-1]+list_numbers[i-1]
    return prefixsum



n=int(input())
list_num=[int(i) for i in input().split()]
new_num=makeprefixsum(list_num)
if n==1:
    count_min=0
else:
    count_min=0
    for j in range(1,n):
        count_min+=j*list_num[j]
    count=count_min
    for i in range(1,n):
        count+=new_num[i]-(new_num[n]-new_num[i])
        if count<count_min:
            count_min=count

print(count_min)


