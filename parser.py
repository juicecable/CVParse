#Copyright Derek Frombach
f=open('data.txt','r')
data=f.read()
f.close()
lines=data.splitlines()
i=0
cid=0
conf=0.0
l=0
r=0
b=0
t=0
w=0
h=0
a=0
c=''
cx=0
cy=0
for line in lines:
    lf=line.find
    if lf('detectNet.Detection object')>=0:
        i=1
    elif i==1 and lf('ClassID')>=0:
        cid=int(float(line[9+lf('ClassID'):].rstrip().lstrip()))
        i=2
    elif i==2 and lf('Confidence')>=0:
        conf=float(line[12+lf('Confidence'):].rstrip().lstrip())
        i=3
    elif i==3 and lf('Left')>=0:
        l=int(float(line[6+lf('Left'):].rstrip().lstrip()))
        i=4
    elif i==4 and lf('Top')>=0:
        t=int(float(line[5+lf('Top'):].rstrip().lstrip()))
        i=5
    elif i==5 and lf('Right')>=0:
        r=int(float(line[7+lf('Right'):].rstrip().lstrip()))
        i=6
    elif i==6 and lf('Bottom')>=0:
        b=int(float(line[8+lf('Bottom'):].rstrip().lstrip()))
        i=7
    elif i==7 and lf('Width')>=0:
        w=int(float(line[7+lf('Width'):].rstrip().lstrip()))
        i=8
    elif i==8 and lf('Height')>=0:
        h=int(float(line[8+lf('Height'):].rstrip().lstrip()))
        i=9
    elif i==9 and lf('Area')>=0:
        a=int(float(line[6+lf('Area'):].rstrip().lstrip()))
        i=10
    elif i==10 and lf('Center')>=0:
        c=((line[8+lf('Center'):].rstrip().lstrip())[1:-1]).split(', ')
        cx=int(float(c[0]))
        cy=int(float(c[1]))
        i=0

print(cid)
print(conf)
print(l)
print(r)
print(b)
print(t)
print(w)
print(h)
print(a)
print(cx)
print(cy)
