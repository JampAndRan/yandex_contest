n=int(input())
list_a=[int(i) for i in input().split()]
list_b=[int(i) for i in input().split()]
list_p=[int(i) for i in input().split()]

list_alg=[[0] for i in range (n)]
for i in range(n):
    dict_alg={}
    dict_alg["a"]=list_a[i]
    dict_alg["b"] = list_b[i]
    dict_alg["number"] = i+1
    list_alg[i]=dict_alg

list_alg_sort_a=sorted(list_alg, key=lambda x: (x["a"],x["b"],-x["number"]),reverse=True)
list_alg_sort_b=sorted(list_alg, key=lambda x: (x["b"],x["a"],-x["number"]),reverse=True)

set_number=set()

l_a=0
l_b=0

for j in range(n):
    if list_p[j]==0:
        if list_alg_sort_a[l_a]["number"] not in set_number:
            num=list_alg_sort_a[l_a]["number"]
            l_a+=1
            set_number.add(num)
            if j==n-1:
                print(num)
            else:
                print(num, end=" ")
        else:
            while list_alg_sort_a[l_a]["number"] in set_number:
                l_a += 1
            num = list_alg_sort_a[l_a]["number"]
            l_a += 1
            set_number.add(num)
            if j == n - 1:
                print(num)
            else:
                print(num, end=" ")
    else:
        if list_alg_sort_b[l_b]["number"] not in set_number:
            num=list_alg_sort_b[l_b]["number"]
            l_b+=1
            set_number.add(num)
            if j==n-1:
                print(num)
            else:
                print(num, end=" ")
        else:
            while list_alg_sort_b[l_b]["number"] in set_number:
                l_b += 1
            num = list_alg_sort_b[l_b]["number"]
            l_b += 1
            set_number.add(num)
            if j == n - 1:
                print(num)
            else:
                print(num, end=" ")



