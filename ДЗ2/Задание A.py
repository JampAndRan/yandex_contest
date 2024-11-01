def makeprefixsum(list_numbers):
    prefixsum=[0]*(len(list_numbers)+1)
    for i in range(1,len(list_numbers)+1):
        prefixsum[i]=prefixsum[i-1]+list_numbers[i-1]
    return prefixsum


n=int(input())
list_numbers=[int (i) for i in input().split()]
new_num=makeprefixsum(list_numbers)

for num in range(1,len(new_num)):
    print(new_num[num], end=" ")

