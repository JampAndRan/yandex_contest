n=int(input())
stack_x=[]
stack_sum=[0 for i in range(100001)]
for i in range(n):
    s=input()
    if s[0]=="+":
        tin=int(s[1:])
        stack_x.append(tin)
        stack_sum[len(stack_x)]=stack_sum[len(stack_x)-1]+tin
    elif s[0]=="-":
        stack_sum[len(stack_x)]=0
        print(stack_x.pop())
    else:
        k=int(s[1:])
        pref=stack_sum[len(stack_x)]-stack_sum[len(stack_x)-k]
        print(pref)


