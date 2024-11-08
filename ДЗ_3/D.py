set_q={"+","*","-"}

s=input().split()
list_c=[]
for i in range(len(s)):
    if s[i] not in set_q:
        list_c.append(int(s[i]))
    else:
        list_c.append(s[i])

def stack_cyf(s, set_q):
    stack_list=[]
    for i in range (len(s)):
        if s[i] not in set_q:
            stack_list.append(s[i])
        else:
            a=stack_list.pop()
            b=stack_list.pop()
            if s[i]=="+":
                c=b+a
            elif s[i]=="*":
                c=b*a
            else:
                c=b-a
            stack_list.append(c)
    return stack_list[0]

kek=stack_cyf(list_c, set_q)
print(kek)
