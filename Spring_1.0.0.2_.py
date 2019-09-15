import binascii
import json
block=147456
blockw=147455
blockw1=16384
virationc=16383
bitc=14
a=0
qfl=0
h=0
lenf1=0
byteb=""
notexist=""
lenf=0
numberschangenotexistq = []
qwa=0
z=0
m = []
p=0
asd=""
b=0
szx=""
asf2="0b"
while b<blockw1:
    m+=[-1]
    b=b+1
k = []
wer=""
numberschangenotexist = []
numbers = []
name = input("What is name of file? ")
namea="file.Spring"
namem=name+"/"
s=""
qwt=""
sda=""
ert=0
aqwer=0
aqwq=0
aqwers=0
qwaw=""
with open(namea, "w") as f4:
    f4.write(s)
with open(namea, "a") as f3:
    f3.write(namem)
with open(name, "rb") as binary_file:
    data = binary_file.read()
    lenf1=len(data)
    if lenf1<2500000:
        print("This file is too small");
        raise SystemExit
    s=str(data)
    lenf=len(data)
sda=bin(int(binascii.hexlify(data),16))[2:]
szx=""
lenf=len(sda)
xc=8-lenf%8
z=0
if xc!=0:
    if xc!=8:
        while z<xc:
            szx="0"+szx
            z=z+1
sda=szx+sda     
lenf=len(sda)
szx=""
for byte in sda:
    aqwer=aqwer+1
    aqwers=aqwers+1
    qwaw=qwaw+byte
    if aqwer<=bitc:
        qwt=qwt+byte
    if aqwer==bitc:
        aqwq=int(qwt,2)
        qwt=""
        a=a+1
        h=h+1  
    av=bin(aqwq)
    if a<=block and aqwer==bitc:
        aqwer=0
        m[aqwq] = aqwq
        numbers.append(aqwq)  
    if a == block:
        qwaw=""
        p=0
        while p<blockw1:
            if p!=m[p]:
                k.append(p)     
            p=p+1
        lenfg=len(k)
        if lenfg>0:
            sw=0
            mm=0
            while lenfg<sw or mm==1:
                notexist=k[sw]
                if notexist>1807 and notexist<=10000:
                    notexist=notexist-1808
                    mm=1
                sw=sw+1
                
            szx=bin(notexist)[2:]
            lenf=len(szx)
            if lenf>13:
                raise SystemExit
            notexist=notexist+1808
            xc=13-lenf
            z=0
            if xc!=0:
                while z<xc:
                    szx="0"+szx
                    z=z+1
            wer=wer+szx
            lenf=len(szx)  
            szx=""  
        if lenfg==0:
            raise SystemExit
        b=-1
        kl=block
        cb=0        
        er=-1
        ghj=0
        ghjd=1
        bnk=1
        p=0
        cvz=0
        qwa=qwa+1
        for p in range(blockw):
            if lenfg>0:
                if virationc!=numbers[p]:
                    byteb=numbers[p]
                    numberschangenotexist.append(byteb)
                if virationc==numbers[p]:
                    numberschangenotexist.append(notexist)    
            ghj=numberschangenotexist[p]
            qfl=qfl+1
            ghjd=ghj
            bnk=1
            bnkd=1        
            kl=kl-1
            if qwa<=1:
                if kl>0:
                    bnk=pow(virationc,kl)
                if kl==0:
                    bnk=1          
            if qwa<=1:
                numberschangenotexistq.append(bnk)    
            if lenfg>0:
                bnk=numberschangenotexistq[p]
                ghjd=0
                ghjd=ghj*bnk
            cvz=cvz+ghjd
        szx=bin(cvz)[2:]
        cvz=0
        lenf=len(szx)
        if lenfg>0:
            xc=2064370-lenf
            z=0
            if xc!=0:
                while z<xc:
                    szx="0"+szx
                    z=z+1
            wer=wer+szx
            lenf=len(szx)  
            szx=""   
        a=0
        numberschangenotexist = []    
        del k[:]     
        del numbers[:]
        m = []
        b=0
        while b<blockw1:
            m+=[-1]
            b=b+1
        b=0
        
a=0       
wer=wer+qwaw
qwaw=""
wer="1"+wer+"1"
lenf=len(wer)
xc=8-lenf%8
z=0
if xc!=0:
    if xc!=8:
        while z<xc:
            szx="0"+szx
            z=z+1
wer=wer+szx
lenf=len(szx)                      
szx=""        
wer="0b"+wer
n = int(wer, 2)
jl=binascii.unhexlify('%x' % n)
with open(namea, "ab") as f2ww:             
    f2ww.write(jl)        
        
                
                     
                    
                
          
                   
