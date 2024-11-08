s=input()
list_scoba=[]


def scoba(s):
    list_scoba = []
    for i in s:
        if i=="(" or i=="[" or i=="{":
            list_scoba.append(i)
        else:
            if len(list_scoba)==0:
                return "no"
            else:
                if i==")" and list_scoba[len(list_scoba)-1] =="(":
                    list_scoba.pop()
                elif i=="]" and list_scoba[len(list_scoba)-1] =="[":
                    list_scoba.pop()
                elif i=="}" and list_scoba[len(list_scoba)-1] =="{":
                    list_scoba.pop()
                else:
                    return "no"
    if len(list_scoba)>0:
        return "no"
    else:
        return "yes"

koba=scoba(s)
print(koba)



