from random import randint
def i_contest2(n,list_a,list_b,list_p):
    set_numb = set()
    k=[]
    for i in range(n):
        if list_p[i] == 0:
            max_a = 0
            max_b = 0
            min_numb = n + 1
            for j in range(len(list_a)):
                if j + 1 in set_numb:
                    continue
                else:
                    if list_a[j] > max_a:
                        max_a = list_a[j]
                        max_b = list_b[j]
                        min_numb = j + 1
                    elif list_a[j] == max_a:
                        if list_b[j]> max_b:
                            max_b = list_b[j]
                            min_numb = j + 1
                        elif max_b == list_b[j]:
                            if j + 1 < min_numb:
                                min_numb = j + 1
            set_numb.add(min_numb)
            k.append(min_numb)
        else:
            max_a = 0
            max_b = 0
            min_numb = n + 1
            for j in range(len(list_b)):
                if j + 1 in set_numb:
                    continue
                else:
                    if list_b[j] > max_b:
                        max_b = list_b[j]
                        max_a = list_a[j]
                        min_numb = j + 1
                    elif list_b[j] == max_b:
                        if list_a[j] > max_a:
                            max_a = list_a[j]
                            min_numb = j + 1
                        elif max_a == list_a[j]:
                            if j + 1 < min_numb:
                                min_numb = j + 1
            set_numb.add(min_numb)
            k.append(min_numb)
    return k

def i_contest(n,list_a,list_b,list_p):
    list_alg=[[0] for t in range (n)]
    for i in range(n):
        dict_alg={}
        dict_alg["a"]=list_a[i]
        dict_alg["b"] = list_b[i]
        dict_alg["number"] = i+1
        list_alg[i]=dict_alg

    list_alg_sort_a=sorted(list_alg, key=lambda x: (x["a"],x["b"],-x["number"]),reverse=True)
    list_alg_sort_b=sorted(list_alg, key=lambda x: (x["b"],x["a"],-x["number"]),reverse=True)

    set_number=set()
    k=[]

    l_a=0
    l_b=0

    for j in range(n):
        if list_p[j]==0:
            if list_alg_sort_a[l_a]["number"] not in set_number:
                num=list_alg_sort_a[l_a]["number"]
                l_a+=1
                set_number.add(num)
                k.append(num)
            else:
                while list_alg_sort_a[l_a]["number"] in set_number:
                    l_a += 1
                num = list_alg_sort_a[l_a]["number"]
                l_a += 1
                set_number.add(num)
                k.append(num)
        else:
            if list_alg_sort_b[l_b]["number"] not in set_number:
                num=list_alg_sort_b[l_b]["number"]
                l_b+=1
                set_number.add(num)
                k.append(num)
            else:
                while list_alg_sort_b[l_b]["number"] in set_number:
                    l_b += 1
                num = list_alg_sort_b[l_b]["number"]
                l_b += 1
                set_number.add(num)
                k.append(num)
    return k


count=0
list56=[randint(1,1000) for i in range(100)]
for i in range(len(list56)):
    list1=[randint(1,1000) for j in range(list56[i]) ]
    list2=[randint(1,1000) for j in range(list56[i]) ]
    list3=[randint(0,1) for j in range(list56[i]) ]
    if i_contest(list56[i],list1,list2,list3)!=i_contest2(list56[i],list1,list2,list3):
        count+=1
        print(list1)
        print(list2)
        print(list3)
        print(i_contest(list56[i],list1,list2,list3))
        print(i_contest2(list56[i],list1,list2,list3))

print(count)

