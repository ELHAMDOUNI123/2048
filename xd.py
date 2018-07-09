def codeL(a,b,c,d):
    x=0#pop and for len just append dude
    while x<5 :
        if d=="0":d,c,b,a=c,b,a,"0"
        if b=="0":b,a=a,"0"
        if c=="0":c,b,a=b,a,"0"
        if d=="0":d,c,b,a=c,b,a,"0"
        x+=1
    return a,b,c,d
def codeeL(a,b,c,d):
    if a==b:
        a="0"
        b=str(eval(b)*2)
    if c==b:
        c=str(eval(c)*2)
        b,a=a,"0"           
    if d==c:
        d=str(eval(d)*2)
        c,b,a=b,a,"0"
    return a,b,c,d
def codeeeL(a,b,c,d):
   a,b,c,d=(codeL(a[0],a[2],a[4],a[6])),(codeL(b[0],b[2],b[4],b[6])),(codeL(c[0],c[2],c[4],c[6])),(codeL(d[0],d[2],d[4],d[6]))
   a,b,c,d=(codeeL(a[0],a[1],a[2],a[3])),(codeeL(b[0],b[1],b[2],b[3])),(codeeL(c[0],c[1],c[2],c[3])),(codeeL(d[0],d[1],d[2],d[3]))

def codeeeR(a,b,c,d):
   a,b,c,d=(codeL(a[0],a[2],a[4],a[6])),(codeL(b[0],b[2],b[4],b[6])),(codeL(c[0],c[2],c[4],c[6])),(codeL(d[0],d[2],d[4],d[6]))
   a,b,c,d=(codeeL(a[0],a[1],a[2],a[3])),(codeeL(b[0],b[1],b[2],b[3])),(codeeL(c[0],c[1],c[2],c[3])),(codeeL(d[0],d[1],d[2],d[3]))   
   if a[0]=="0":
       if a[1]=="0":
           a=[a[3],a[2],"0","0"]
       else:a=[a[3],a[2],a[1],"0"]
   if b[0]=="0":
       if b[1]=="0":
           b=[b[3],b[2],"0","0"]
       else:b=[b[3],b[2],b[1],"0"]
   if c[0]=="0":
       if c[1]=="0":
           c=[c[3],c[2],"0","0"]
       else:c=[c[3],c[2],c[1],"0"]
   if d[0]=="0":
       if d[1]=="0":
           d=[d[3],d[2],"0","0"]
       else:d=[d[3],d[2],d[1],"0"]
   print (a) 
   print (b)
   print (c)
   print (d)       
    
a,b,c,d,e= input(),input(),input(),input(),input()
if e=="L":
    codeeeL(a,b,c,d)
if e=="R":
    codeeeR(a,b,c,d)
if e=="U":
    codeeeL(a,b,c,d)
    
 
if e=="K":
    codeeeR(a,b,c,d)
    print ("------")
    codeeeL(a,b,c,d)
