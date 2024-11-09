import collections

n=int(input())
a,b=map(int,input().split())
list_n=[0 for i in range(n)]

dq1 = collections.deque()
dq2 = collections.deque()
dq3 = collections.deque()
dq4 = collections.deque()
dq1_list=[]
dq2_list=[]
dq3_list=[]
dq4_list=[]

if abs(a-b)==2:
    for i in range(n):
        c, d = map(int, input().split())
        if c == a:
            dq1_list.append([d, i])
        elif c == b:
            dq2_list.append([d, i])
        elif c == (a+b)//2:
            dq3_list.append([d, i])
        else:
            dq4_list.append([d, i])
else:
    if a==1 and b==2 or a==2 and b==1:
        for i in range(n):
            c, d = map(int, input().split())
            if c == 1:
                dq1_list.append([d, i])
            elif c == 2:
                dq2_list.append([d, i])
            elif c == 3:
                dq3_list.append([d, i])
            else:
                dq4_list.append([d, i])
    if a==1 and b==4 or a==4 and b==1:
        for i in range(n):
            c, d = map(int, input().split())
            if c == 4:
                dq1_list.append([d, i])
            elif c == 1:
                dq2_list.append([d, i])
            elif c == 2:
                dq3_list.append([d, i])
            else:
                dq4_list.append([d, i])
    if a==2 and b==3 or a==3 and b==2:
        for i in range(n):
            c, d = map(int, input().split())
            if c == 2:
                dq1_list.append([d, i])
            elif c == 3:
                dq2_list.append([d, i])
            elif c == 4:
                dq3_list.append([d, i])
            else:
                dq4_list.append([d, i])
    if a==3 and b==4 or a==4 and b==3:
        for i in range(n):
            c, d = map(int, input().split())
            if c == 3:
                dq1_list.append([d, i])
            elif c == 4:
                dq2_list.append([d, i])
            elif c == 1:
                dq3_list.append([d, i])
            else:
                dq4_list.append([d, i])


dq1_list_new=sorted(dq1_list, key=lambda x: (x[0],x[1]))
dq2_list_new=sorted(dq2_list, key=lambda x: (x[0],x[1]))
dq3_list_new=sorted(dq3_list, key=lambda x: (x[0],x[1]))
dq4_list_new=sorted(dq4_list, key=lambda x: (x[0],x[1]))


for i in dq1_list_new:
    dq1.append(i)
for i in dq2_list_new:
    dq2.append(i)
for i in dq3_list_new:
    dq3.append(i)
for i in dq4_list_new:
    dq4.append(i)


t=1
c=0

if abs(a-b)==2:
    while len(dq1)>0 or len(dq2)>0 or len(dq3)>0 or  len(dq4)>0:
        if len(dq1) > 0:
            if dq1[0][0] <= t:
                list_n[dq1[0][1]] = t
                dq1.popleft()
                c=-1
        if len(dq2) > 0:
            if dq2[0][0] <= t:
                list_n[dq2[0][1]] = t
                dq2.popleft()
                c=-1
        if c==-1:
            t+=1
            c=0
            continue
        else:
            if len(dq3) > 0:
                if dq3[0][0] <= t:
                    list_n[dq3[0][1]] = t
                    dq3.popleft()
            if len(dq4) > 0:
                if dq4[0][0] <= t:
                    list_n[dq4[0][1]] = t
                    dq4.popleft()
        t+=1
else:
    while len(dq1)>0 or len(dq2)>0 or len(dq3)>0 or  len(dq4)>0:
        if len(dq1) > 0:
            if dq1[0][0] <= t:
                list_n[dq1[0][1]] = t
                dq1.popleft()
                t+=1
                continue
        if len(dq2) > 0:
            if dq2[0][0] <= t:
                list_n[dq2[0][1]] = t
                dq2.popleft()
                t += 1
                continue
        if len(dq3) > 0:
            if dq3[0][0] <= t:
                list_n[dq3[0][1]] = t
                dq3.popleft()
                t += 1
                continue
        if len(dq4) > 0:
            if dq4[0][0] <= t:
                list_n[dq4[0][1]] = t
                dq4.popleft()
        t+=1

for i in list_n:
    print(i)








