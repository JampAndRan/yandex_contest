n, c=map(int,input().split())
s=input()

def cars(s, c):
    if len(s)==1:
        return 1
    else:
        max_count=0
        boor=0
        count = 0
        last=0
        dict_c={"a":0, "b":0}
        for first in range(len(s)):
            while last<len(s) and boor<=c:
                if s[last]=="a":
                    dict_c["a"]+=1
                if s[last]=="b":
                    dict_c["b"]+=1
                    boor+= dict_c["a"]
                    if boor>c:
                        break
                count+=1
                if count>=max_count:
                    max_count=count
                last+=1
            if len(s)==last:
                return max_count
            else:
                if s[last]=="a":
                    dict_c["a"]-=1
                if s[last]=="b":
                    dict_c["b"]-=1
                boor -= dict_c["a"]
                count -= 1
                if s[first]=="b":
                    dict_c["b"] -= 1
                elif s[first]=="a":
                    dict_c["a"] -= 1
                    boor-=dict_c["b"]
        return max_count


max_count=cars(s,c)
print(max_count)
