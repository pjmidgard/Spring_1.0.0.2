import binascii
import json
a=0
b=0
dd=0
ertf=0
l=""
j=0
b=0
aq=0
qfl=0
t=0
h=0
byteb=""
notexist=""
lenf=0
numberschangenotexistq = []
numberschangenotexistqz = []
qwa=0
m = []
p=0
r=0
namea=""
asd=""
b=0
szx=""
asf2="0b"
while b<65536:
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
ertfa=0 
aqwer=0
aqwq=0
aqwq=0
with open(namea, "w") as f4:
        f4.write(s)
with open(namea, "a") as f3:
        f3.write(namem)
with open(name, "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    
    s=str(data)
    lenf=len(data)
    
    with open(namea, "ab") as f2:
        
        while dd<1:
            dd=dd+1
            sda=bin(int(binascii.hexlify(data),16))[2:]
            a=0
            ertfa=0 
            b=0
            ertf=0
            l=""
            j=0
            b=0
            aq=0
            qfl=0
            t=0
            h=0
            byteb=""
            notexist=""
            lenf=0
            m = []
            p=0
            namea=""
            asd=""
            b=0
            szx=""
            asf2="0b"
            while b<65536:
                m+=[-1]
                b=b+1
            k = []
            wer=""
            numberschangenotexist = []
            numbers = []
            for byte in sda:
                aqwer=aqwer+1
                if aqwer<=13:
                    qwt=qwt+byte
                if aqwer==13:
                    aqwq=int(qwt,2)
                    qwt=""
                    a=a+1
                    h=h+1
                    
                        
                av=bin(aqwq)
                   
                if a<=65536 and aqwer==13:
                    aqwer=0
                    m[aqwq] = aqwq
                    numbers.append(aqwq)
                        
                        
                if a == 65536:
                    p=0
                    while p<8192:
                        if p!=m[p]:
                            k.append(p)
                                
                        p=p+1
                        
                    #lenf count
                    lenfg=len(k)

                    if lenfg==0:
                       ertfa=0
                    if lenfg!=0:
                        ertf=ertf+1
                        if ertf==1:
                            ertfa=1
                            ertf=0
                        if ertf==2:
                            ertfa=1
                            ertf=0
                        notexist=k[0]
                        
                        szx=bin(notexist)[2:]
                        lenf=len(szx)
                        if lenf>10:
                            lenfg=0    
                   
                    if ertfa!=1:
                        lenfg=0
                        ertfa=0
                        ertf=0
                    elif ertf==2:
                        wer=wer+"0"
                        ertfa=0
                        ertf=0
                            
                    
                        
                    print(lenfg)

                    if lenfg>0:
                        wer=wer+"0" 
                       
                        
                        xc=10-lenf
                        z=0
                        if xc!=0:
                            while z<xc:
                                szx="0"+szx
                                z=z+1
                        wer=wer+szx
                        lenf=len(szx)
                            
                        szx=""
                            
                           
                    if lenfg==0:
                       wer=wer+"1" 
                    b=-1
                    bb=0
                    kl=65536
                    bnk=0
                    cb=0
                        
                               
                    bb=-1
                    er=-1
                    ghj=0
                    ghjd=1
                    bnk=1
                    p=-1
                    cvz=0
                    qwa=qwa+1
                    while p<65535:
                        p=p+1
                        if lenfg>0:
                            if 8191!=numbers[p]:
                                byteb=numbers[p]
                                numberschangenotexist.append(byteb)
                            if 8191==numbers[p]:
                                numberschangenotexist.append(notexist)
                        if lenfg==0:
                            byteb=numbers[p]
                            numberschangenotexist.append(byteb)
                            
                            #count 1779
                         
                          
                            
                            
                                
                        ghj=numberschangenotexist[p]
                        qfl=qfl+1
                        ghjd=ghj
                        bnk=1
                        bnks=1
                        bb=-1
                        bnkd=1
                               
                                    
                        kl=kl-1
                        if qwa<=1:
            
                            if qwa<=1:
                                bb=bb+1
                                    
                                        
                            if qwa<=1:
                                if kl>0:
                                    bnk=8191**kl
                                if kl==0:
                                    bnk=1
                                    
                                       
                            if qwa<=1:
                                if kl>0:
                                    bnks=8192**kl
                                if kl==0:
                                    bnks=1
                              
                                
                                        
                        if qwa<=1:
                            numberschangenotexistq.append(bnk)
                            numberschangenotexistqz.append(bnks)
                        if lenfg>0:
                            bnk=numberschangenotexistq[p]
                            ghjd=0
                            ghjd=ghj*bnk
                        if lenfg==0:
                            bnks=numberschangenotexistqz[p]
                            ghjd=0
                            ghjd=ghj*bnks
                        cvz=cvz+ghjd
                    szx=bin(cvz)[2:]
                    lenf=len(szx)
                    print(lenf)
                    
                    
                    
                        
                        
                       
                    if lenfg>0:
                        xc=851957-lenf
                        z=0
                        if xc!=0:
                            while z<xc:
                                szx="0"+szx
                                z=z+1
                        wer=wer+szx
                        lenf=len(szx)
                            
                            
                            
                        szx=""
                    if lenfg==0:
                        xc=851968-lenf
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
                    while b<28672:
                        m+=[-1]
                        b=b+1
                    b=0
                    b=0
                               
                                
                r=h%65536
            if r!=0:
                    
                r=r-1
                p=-1
                if r!=65535:
                    b=-1
                    bb=0
                    kl=r+1
                    bnk=0
                    cb=0
                    er=0
                                           
                    bb=-1
                    cvz=0
                    ghj=0
                    ghjd=1
                    bnk=1
                    while p<r:
                        p=p+1
                        byteb=numbers[p]
                        numberschangenotexist.append(byteb)
                            
                                    #count 1789
                          
                           
                                
                                          
                                            
                                                
                            
                            
                            
                                            
                        ghj=numberschangenotexist[b]         
                        ghjd=ghj
                        bnk=1
                        bb=-1
                        kl=kl-1
                        if kl>0:   
                            bnk=8192**kl
                        if kl==0:
                            bnks=1
                        ghjd=0
                        ghjd=ghj*bnk
                        cvz=cvz+ghjd
                    szx=bin(cvz)[2:]
                    lenf=len(szx)
                           
                    ert=0
                    r=r+1
                    ert=r*8
                            
                    xc=ert-lenf
                    z=0
                    if xc!=ert:
                        while z<xc:
                            szx="0"+szx
                            z=z+1
                        wer=wer+szx
                        lenf=len(szx)
                                
                        szx=""
            lenf=len(qwt)
            if lenf!=0:
                aqwq=int(qwt,2)
                szx=bin(aqwq)[2:]
                lenf=len(szx)
            wer=wer+szx
            szx=""
            szx=bin(lenf)[2:]
            wer=wer+szx
            szx=""
            xc=4-lenf
            if xc!=0:
                while z<xc:
                    szx="0"+szx
                    z=z+1
                wer=wer+szx
                lenf=len(szx)
                szx=""
                                
                                
                         
                        
            a=0 
                    
                    
            wer="0b1"+wer+"1"


            lenf=len(wer)
            xc=8-lenf%8
            z=0
            if xc!=ert:
                while z<xc:
                    szx="0"+szx
                    z=z+1
                wer=wer+szx
                lenf=len(szx)
                                    
                szx=""        
                
                        
            n = int(wer, 2)
            jl=binascii.unhexlify('%x' % n)
            data=jl   
        f2.write(jl)        
        
                
                     
                    
                
          
                   
