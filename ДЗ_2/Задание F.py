n=int(input())
list_numbers=[int (i) for i in input().split()]
summ=sum(list_numbers)
summ2=0
for i in list_numbers:
    summ2+=i**2

count=0
for i in list_numbers:
    kek=i*((summ-i)*summ-(summ-i)*i-(summ2-i**2))
    count+=kek




count=count//6
count=count%1000000007
print(count)
