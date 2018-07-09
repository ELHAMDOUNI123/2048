def codeL(a,b,c,d):
    x=0
    while x<6 :

        if d=="0":d,c,b,a=c,b,a,"0"
        if b=="0":b,a=a,"0"
        if c=="0":c,b,a=b,a,"0"
        if d=="0":d,c,b,a=c,b,a,"0"
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
        elif c==b:
            a,b,c="0","0",(int(c)+int(b))
            c*=2
            break
        if d==c:
            a,b,d="0","0",(int(c)+int(d))
            d*=2
            break
        m+=1
    return a,b,c,d
def codeeeL(a,b,c,d):
   a,b,c,d=(codeL(a[0],a[2],a[4],a[6])),(codeL(b[0],b[2],b[4],b[6])),(codeL(c[0],c[2],c[4],c[6])),(codeL(d[0],d[2],d[4],d[6]))
   print ((codeeL(a[0],a[1],a[2],a[3])),(codeeL(b[0],b[1],b[2],b[3])),(codeeL(c[0],c[1],c[2],c[3])),(codeeL(d[0],d[1],d[2],d[3])))
a,b,c,d,e= input(),input(),input(),input(),input()
if e=="L":
    print(codeeeL(a,b,c,d))

                                                                
def codeR(a,b,c,d):
    x=0#pop and for len just append dude
    while x<5 :
        if d=="0":d,c,b,a=c,b,a,"0"
        if b=="0":b,a=a,"0"
        if c=="0":c,b,a=b,a,"0"
        if d=="0":d,c,b,a=c,b,a,"0"
        x+=1
    return a,b,c,d
