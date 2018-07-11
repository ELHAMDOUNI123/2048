import random 
a = [str(x) for x in input().split()]
b = [str(x) for x in input().split()]
c = [str(x) for x in input().split()]
d = [str(x) for x in input().split()]
a1,b1,c1,d1=a,b,c,d
ex=4
ey=4
def RL(a,b,c,d):
    for i in (a,b,c,d):
        while "0" in i:
            i.remove("0")
        j=0
        while j<(len(i)-1)  :
            if i[j]==i[j+1]:
                i[j+1]=str(int(i[j])*2)
                i.remove(i[j])
            j+=1
        if O=="R":
            for x in range (len(i),ex):i.append("0")
        elif O=="U":
            for x in range (len(i),ex):i.append("0")
        elif O=="L":
            for x in range (len(i),ey):i.insert(0,"0")
        elif O=="D":
            for x in range (len(i),ey):i.insert(0,"0")
    return a,b,c,d

while 1>0:

    O=input()
    if O=="R":
        RL(a,b,c,d)
        print (a) 
        print (b)
        print (c)
        print (d)
    if O=="L":
        RL(a,b,c,d)
        print (a) 
        print (b)
        print (c)
        print (d)
    if O=="U":
        a=[a[0],b[0],c[0],d[0]]
        b=[a1[1],b1[1],c1[1],d1[1]]
        c=[a1[2],b1[2],c1[2],d1[2]]
        d=[a1[3],b1[3],c1[3],d1[3]]
        RL(a,b,c,d)
        a2,b2,c2,d2=a,b,c,d
        a=[a[0],b[0],c[0],d[0]]
        b=[a2[1],b2[1],c2[1],d2[1]]
        c=[a2[2],b2[2],c2[2],d2[2]]
        d=[a2[3],b2[3],c2[3],d2[3]]
        print (a) 
        print (b)
        print (c)
        print (d)
    if O=="D":
        a=[a[0],b[0],c[0],d[0]]
        b=[a1[1],b1[1],c1[1],d1[1]]
        c=[a1[2],b1[2],c1[2],d1[2]]
        d=[a1[3],b1[3],c1[3],d1[3]]
        RL(a,b,c,d)
        a2,b2,c2,d2=a,b,c,d
        a=[a[0],b[0],c[0],d[0]]
        b=[a2[1],b2[1],c2[1],d2[1]]
        c=[a2[2],b2[2],c2[2],d2[2]]
        d=[a2[3],b2[3],c2[3],d2[3]]
        print (a) 
        print (b)
        print (c)
        print (d)
    r=(random.choice(['2','2','4']))
    m=(random.choice([a,b,c,d]))
    n=(random.choice([0,1,2,3]))
    while m[n]!="0":
        m=(random.choice([a,b,c,d]))
        n=(random.choice([0,1,2,3]))

    m[n]=r
    if "0" not in a and "0"not in b and "0" not in c and "0" not in d:
        print "GAME OVER"
        break
