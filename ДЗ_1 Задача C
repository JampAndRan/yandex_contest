n=int(input())
list_resh=[['.']*n for i in range(n)]

for i in range(n):
    s=input()
    for j in range(n):
        list_resh[j][n-1-i]=s[j]

def search_key(x1,y1,x2, y2,list_resh):
    x3=30
    y3=30
    x4=-1
    y4=-1
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if list_resh[x][y] == "." and y < y3:
                x3 = x
                y3 = y
            elif list_resh[x][y] == "." and y == y3 and x < x3:
                x3 = x
            if list_resh[x][y] == "." and y > y4:
                x4 = x
                y4 = y
            elif list_resh[x][y] == "." and y == y4 and x > x4:
                x4 = x
    return x3,y3,x4,y4


x1=30
y1=30
x2=-1
y2=-1

for x in range(n):
    for y in range(n):
        if y>y2 and list_resh[x][y]=="#":
            y2=y
        if x>x2 and list_resh[x][y]=="#":
            x2=x
        if y<y1 and list_resh[x][y]=="#":
            y1=y
        if x<x1 and list_resh[x][y]=="#":
            x1 = x

if x1==30:
    print("X")
else:
    t=0
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if list_resh[x][y]==".":
                t+=1
    if t==0:
        print("I")
    else:
        if list_resh[x2][y2]==".":
            x3, y3, x4, y4 = search_key(x1, y1, x2, y2, list_resh)
            if x3==30 or x1>=x3 or x3>x4 or x4!=x2 or y1>=y3 or y3>y4 or y4!=y2:
                print("X")
            else:
                t=0
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        if (x<x3 or y<y3) and list_resh[x][y]==".":
                            t+=1
                        elif x>=x3 and y>=y3 and list_resh[x][y]=="#":
                            t+=1
                if t == 0:
                    print("L")
                else:
                    print("X")
        else:
            t=0
            y=y2
            for x in range(x1,x2):
                if list_resh[x][y]==".":
                    t=-1
            if t==-1:
                l=-1
                for y in range(y1,y2+1):
                    p=0
                    for x in range(x1,x2+1):
                        if list_resh[x][y]==".":
                            p+=1
                    if p==0:
                        l=y
                if l==-1:
                    print("X")
                else:
                    x5,y5,x6,y6 = search_key(x1, l+1, x2, y2, list_resh)
                    x3, y3, x4, y4 = search_key(x1, y1, x2, l-1, list_resh)

                    if x3==30 or x5==30 or x1>=x3 or x3!=x5 or x5>x4 or x4!=x6 or x6>=x2 or y1!=y3 or y3>y4 or y4>y5 or y6!=y2:
                        print("X")
                    else:
                        q=0
                        for x in range(x1,x2+1):
                            for y in range(y1,y2+1):
                                if x>=x5 and x<=x6 and y>=y5 and y<=y6 or  x>=x3 and x<=x4 and y>=y3 and y<=y4:
                                    if list_resh[x][y] == "#":
                                        q+=1
                                else:
                                    if list_resh[x][y] == ".":
                                        q+=1
                        if q!=0:
                            print("X")
                        else:
                            print("H")
            else:
                if list_resh[x2][y1] == ".":
                    l = -1
                    for y in range(y1, y2 + 1):
                        p = 0
                        for x in range(x1, x2 + 1):
                            if list_resh[x][y] == ".":
                                p += 1
                        if p == 0:
                            l = y
                            break
                    if l == -1 or l==y2:
                        print("X")
                    else:
                        x5, y5, x6, y6 = search_key(x1, l+1, x2, y2, list_resh)
                        x3, y3, x4, y4 = search_key(x1, y1, x2, l-1, list_resh)
                        if x3==30 or x5==30 or x1>=x3 or x3!=x5 or x5>x6 or x6>=x4 or x4!=x2 or y1!=y3 or y3>y4 or y4>=y5 or y5>y6 or y6>=y2:
                            print("X")
                        else:
                            q = 0
                            for x in range(x1, x2 + 1):
                                for y in range(y1, y2 + 1):
                                    if x >= x5 and x <= x6 and y >= y5 and y <= y6 or x >= x3 and x <= x4 and y >= y3 and y <= y4:
                                        if list_resh[x][y] == "#":
                                            q += 1
                                    else:
                                        if list_resh[x][y] == ".":
                                            q += 1
                            if q != 0:
                                print("X")
                            else:
                                print("P")
                else:
                    x=x2
                    q=0
                    for y in range(y1,y2):
                        if list_resh[x][y] == ".":
                            q += 1
                    if q!=0:
                        x3,y3,x4,y4=search_key(x1,y1,x2, y2,list_resh)
                        if x3==30 or x1>=x3 or x3>x4 or x4!=x2 or y1>=y3 or y3>y4 or y4>=y2:
                            print("X")
                        else:
                            q = 0
                            for x in range(x1, x2 + 1):
                                for y in range(y1, y2 + 1):
                                    if x >= x3 and x <= x4 and y >= y3 and y <= y4:
                                        if list_resh[x][y] == "#":
                                            q += 1
                                    else:
                                        if list_resh[x][y] == ".":
                                            q += 1
                            if q != 0:
                                print("X")
                            else:
                                print("C")
                    else:
                        x3,y3,x4,y4=search_key(x1,y1,x2, y2,list_resh)
                        if x3==30 or x1>=x3 or x3>x4 or x4>=x2 or y1>=y3 or y3>y4 or y4>=y2:
                            print("X")
                        else:
                            q = 0
                            for x in range(x1, x2 + 1):
                                for y in range(y1, y2 + 1):
                                    if x >= x3 and x <= x4 and y >= y3 and y <= y4:
                                        if list_resh[x][y] == "#":
                                            q += 1
                                    else:
                                        if list_resh[x][y] == ".":
                                            q += 1
                            if q != 0:
                                print("X")
                            else:
                                print("O")









