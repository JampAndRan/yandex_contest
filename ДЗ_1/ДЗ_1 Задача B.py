
blue_mayk=int(input())
red_mayk=int(input())
blue_socks=int(input())
red_socks=int(input())


count1=red_mayk+1+red_socks+1
count2=blue_mayk+1+blue_socks+1

if blue_mayk>=red_mayk:
    count3=blue_mayk+2
else:
    count3=red_mayk+2

if blue_socks>=red_socks:
    count4=blue_socks+2
else:
    count4 = red_socks + 2


if blue_mayk==0:
    print(1,blue_socks+1)
elif red_mayk==0:
    print(1,red_socks+1)
elif blue_socks==0:
    print(blue_mayk+1,1)
elif red_socks==0:
    print(red_mayk+1,1)

elif min(count1,count2,count3,count4)==count4:
    if blue_socks>=red_socks:
        print(1, blue_socks+1)
    else:
        print(1, red_socks + 1)

elif min(count1,count2,count3,count4)==count3:
    if blue_mayk>=red_mayk:
        print(blue_mayk+1, 1)
    else:
        print(red_mayk+1, 1)

elif min(count1,count2,count3,count4)==count2:
    print(blue_mayk+1,blue_socks+1)

else:
    print(red_mayk+1,red_socks+1)
