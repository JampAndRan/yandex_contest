n=int(input())
list_towns=[int(i) for i in input().split()]

def stack_towns(list_towns, n):
    new_towns=[[0] for i in range(n)]
    stack_towns=[]
    stack_towns.append([list_towns[0], 0])
    for i in range (1,n):
        if stack_towns[-1][0]<=list_towns[i]:
            stack_towns.append([list_towns[i], i])
        else:
            while stack_towns[-1][0]>list_towns[i] and len(stack_towns)>0:
                new_towns[stack_towns[-1][1]]=i
                stack_towns.pop()
                if len(stack_towns)==0:
                    break
            stack_towns.append([list_towns[i], i])
    while  len(stack_towns)>0:
        new_towns[stack_towns[-1][1]]=-1
        stack_towns.pop()
    return new_towns

new_towns=stack_towns(list_towns, n)
print(*new_towns)


