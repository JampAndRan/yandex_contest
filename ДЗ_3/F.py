n=int(input())
w=input()
s=input()
k=""
k+=s

list_scoba=[]
count=0

for i in s:
    if i=="(" or i=="[":
        list_scoba.append(i)
        count+=1
    else:
        list_scoba.pop()

while count<n//2:
    for j in w:
        if j=="]":
            if len(list_scoba)>0:
                if list_scoba[-1]=="[":
                    k+=j
                    list_scoba.pop()
                    break
        elif j==")":
            if len(list_scoba)>0:
                if list_scoba[-1]=="(":
                    k += j
                    list_scoba.pop()
                    break
        else:
            count+=1
            k+=j
            list_scoba.append(j)
            break

while len(list_scoba)>0:
    if list_scoba[-1]=="(":
        k+=")"
        list_scoba.pop()
    else:
        k += "]"
        list_scoba.pop()

print(k)





