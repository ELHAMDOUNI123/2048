def code(a,b,c,d):
    x=0
    while x<6 :
        if d=="0":d,c,b,a=c,b,a,"0"
        if b=="0":b,a=a,"0"
        elif c=="0":c,b,a=b,a,"0"
        elif d=="0":d,c,b,a=c,b,a,"0"
        x+=1
    return a,b,c,d
def codee(a,b,c,d) :
    m=0
    while m<2: 
        if a==b:
            a,b="0",(int(a)+int(b))
            if d==c:
                d,c,b=(int(c)+int(d)),(b*2),"0"
                break
        if c==b:
            a,b,c="0","0",(int(c)+int(b))
            c*=2
            break
        if d==c:
            a,b,d="0","0",(int(c)+int(d))
            d*=2
            break
        m+=1
    return a,b,c,d
def codeee(a,b,c,d):
   a,b,c,d=(code(a[0],a[2],a[4],a[6])),(code(b[0],b[2],b[4],b[6])),(code(c[0],c[2],c[4],c[6])),(code(d[0],d[2],d[4],d[6]))
   print ((codee(a[0],a[1],a[2],a[3]),(codee(b[0],b[1],b[2],b[3])),(codee(b[0],b[1],b[2],b[3])),(codee(b[0],b[1],b[2],b[3])))

a = input()
b = input()
c = input()
d = input()
e = input()#= input(), input(), input(), input(), input()

if e=="L":
    print(codeee(a,b,c,d))
if e=="R":
    print(code(d,c,b,a))
                                                                

