import collections

dq = collections.deque()



n,k=map(int,input().split())
list_num=[int(i) for i in input().split()]

dq.append(list_num[0])
for i in range(1,k):
    if dq[-1]<=list_num[i]:
        dq.append(list_num[i])
    else:
        while dq[-1]>list_num[i]:
            dq.pop()
            if len(dq) == 0:
                break
        dq.append(list_num[i])

count=0
print(dq[0])
if dq[0]==list_num[count]:
    dq.popleft()
count+=1


for i in range(k,n):
    if len(dq)==0:
        dq.append(list_num[i])
    else:
        if dq[-1]<=list_num[i]:
            dq.append(list_num[i])
        else:
            while dq[-1]>list_num[i]:
                dq.pop()
                if len(dq) == 0:
                    break
            dq.append(list_num[i])
    print(dq[0])
    if dq[0] == list_num[count]:
        dq.popleft()
    count += 1



