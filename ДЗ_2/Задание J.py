def makeprefixsum(list_numbers):
    prefixsum=[0]*(len(list_numbers)+1)
    prefixsum[1]=0
    dict_a={0:1}
    if len(list_numbers)==1:
        return dict_a, prefixsum
    else:
        for i in range(2,len(list_numbers)+1):
            if list_numbers[i-1]==list_numbers[i-2]:
                prefixsum[i]=prefixsum[i-1]+1
                dict_a[prefixsum[i]]=i
            else:
                prefixsum[i] = prefixsum[i - 1]
        return dict_a, prefixsum


def makeprefixsum_sh(list_numbers):
    prefixsum=[0]*(len(list_numbers)+1)
    prefixsum[1]=0
    dict_sh={0:1}
    if len(list_numbers)==1:
        return dict_sh, prefixsum
    else:
        for i in range(2,len(list_numbers)+1):
            if list_numbers[i - 1] < list_numbers[i - 2]:
                prefixsum[i]=prefixsum[i-1]+1
                dict_sh[prefixsum[i]]=i
            else:
                prefixsum[i] = prefixsum[i - 1]
        return dict_sh, prefixsum

n=int(input())
list_a=[int(i) for i in input().split()]
m,k=map(int,input().split())
list_x=[int(i) for i in input().split()]
kim, prefixsum=makeprefixsum(list_a)

dict_sh,prefixsum_sh=makeprefixsum_sh(list_a)

for i in range(m):
    p=list_x[i]
    t = prefixsum[p] - k
    if t < 0:
        t = 0
    if prefixsum_sh[p]==prefixsum_sh[kim[t]]:
        dt = kim[t]
    else:
        dt=dict_sh[prefixsum_sh[p]]
    if i == m - 1:
        print(dt)
    else:
        print(dt, end=" ")
