
from collections import deque


def min_discomfort(n, h, list_h, list_w):
    if n==1:
        return 0
    list_hw = []
    for i in range(n):
        list_hw.append([list_h[i], list_w[i]])
    list_hw_new = sorted(list_hw, key=lambda x: (x[0], x[1]))
    if max(list_w) >= h:
        return 0
    last=1
    current_w=list_hw_new[0][1]
    dq=deque()
    min_abs=pow(10,9)+1
    for i in range(n):
        while current_w<h and last<n:
            current_w += list_hw_new[last][1]
            while dq and dq[-1]<list_hw_new[last][0]-list_hw_new[last-1][0]:
                dq.pop()
            dq.append(list_hw_new[last][0]-list_hw_new[last-1][0])
            last+=1
        if current_w >= h:
            if dq[0] < min_abs:
                min_abs = dq[0]
        current_w-=list_hw_new[i][1]
        if i!=n-1 and dq[0]==list_hw_new[i+1][0]-list_hw_new[i][0]:
            dq.popleft()
    return min_abs


n,h=map(int,input().split())
list_h=[int (i) for i in input().split()]
list_w=[int (i) for i in input().split()]

result = min_discomfort(n, h, list_h, list_w)
print(result)
