sets="0123456789+ *-()"
sets2="+*-"
s=input()


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

def strong(s, sets,sets2):
    q=s.strip()
    if q.isdigit():
        return int(q)
    stack_prob=[]
    count=0
    for i in s:
        if i=="(":
            count+=1
        if i == ")":
            if count==0:
                return "WRONG"
            else:
                count-=1
        if i.isdigit():
            if len(stack_prob)==0:
                stack_prob.append(i)
            elif len(stack_prob) == 2:
                return "WRONG"
        elif i==" ":
            if len(stack_prob)==1:
                stack_prob.append(i)
        else:
            if len(stack_prob)!=0:
                stack_prob = []
        if i not in sets:
            return "WRONG"
    if count !=0:
        return "WRONG"
    s=s.replace(" ","")
    if len(s)<3:
        return "WRONG"
    if s[0] in sets2 or s[-1] in sets2:
        if s[0]=="-":
            if s[1].isdigit():
                s="0"+s
            else:
                return "WRONG"
        else:
            return "WRONG"
    for i in range(1, len(s)-1):
        if s[i] in sets2:
            if s[i-1] in sets2 or s[i-1]=="(":
                if s[i]=="-" and s[i-1]=="(":
                    continue
                else:
                    return "WRONG"
            if s[i + 1] in sets2 or s[i + 1] == ")":
                return "WRONG"
        elif s[i].isdigit():
            if s[i-1]==")" or s[i+1]=="(":
                return "WRONG"
    ct = 0
    for i in range(len(s)):
        if ct==-1:
            if s[i]==")":
                return "WRONG"
            elif s[i] in sets2 or s[i].isdigit():
                ct = 0
        if s[i]=="(":
            ct=-1
    list_numb=[]
    kik=""
    for j in range(len(s)):
        if s[j].isdigit():
                kik+=s[j]
        else:
            if len(kik)>0:
                list_numb.append(int(kik))
                kik=""
                list_numb.append(s[j])
            else:
                if j>0:
                    if s[j-1]=="(" and s[j]=="-":
                        list_numb.append(0)
                        list_numb.append(s[j])
                    else:
                        list_numb.append(s[j])
                else:
                    list_numb.append(s[j])
    if len(kik) > 0:
        list_numb.append(int(kik))
    print(list_numb)
    stack_post=[]
    list_c=[]
    for k in range(len(list_numb)):
        if type(list_numb[k])==int:
            list_c.append(list_numb[k])
        elif list_numb[k]=="(":
            stack_post.append(list_numb[k])
        elif list_numb[k]==")":
            while stack_post[-1]!="(":
                list_c.append(stack_post.pop())
            stack_post.pop()
        elif list_numb[k]=="*":
            if len(stack_post)==0:
                stack_post.append(list_numb[k])
            else:
                while stack_post[-1]=="*":
                    list_c.append(stack_post.pop())
                    if len(stack_post) == 0:
                        break
                stack_post.append(list_numb[k])
        else:
            if len(stack_post)==0:
                stack_post.append(list_numb[k])
            else:
                while stack_post[-1] == "*" or stack_post[-1] == "+" or stack_post[-1] == "-" :
                    list_c.append(stack_post.pop())
                    if len(stack_post) == 0:
                        break
                stack_post.append(list_numb[k])
    while len(stack_post) >0:
        list_c.append(stack_post.pop())
    print(list_c)
    sets2=set(sets2)
    tur=stack_cyf(list_c, sets2)
    return tur


kek=strong(s,sets,sets2)
print(kek)
