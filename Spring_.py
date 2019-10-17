import binascii
a=0
ass=0
asss=0
b=0
aaqw=""
aaqws=""
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
namea=""
d=1
a=0
asd=""
b=0
szx=""
asf2="0b"
while b<1790:
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
with open(namea, "w") as f4:
        f4.write(s)
with open(namea, "a") as f3:
        f3.write(namem)
with open(name, "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    s=str(data)
    lenf1=len(data)
    if lenf1<2000:
        print("This file is too small");
        raise SystemExit
    if lenf1>2**30:
        print("This file is too big");
        raise SystemExit
    with open(namea, "ab") as f2:
        for byte in data:
            av=bin(byte)
            a=a+1
            if a<=1790:
                byte=int(byte)
                m[byte] = byte
                numbers.append(byte)
                h=h+1
                
            if a == 1790:
                p=0
                while p<256:
                    if p!=m[p]:
                        k.append(p)
                        
                    p=p+1
                
                #lenf count
                lenfg=len(k)
                
                

                if lenfg>0:
                  
                    notexist=k[0]    
                    
                    
                   
               
                    
                b=-1
                bb=0
                kl=1789
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
                while p<1789:
                    p=p+1
                    if lenfg>0:
                       if 255!=numbers[p]:
                            byteb=numbers[p]
                            numberschangenotexist.append(byteb)
                       if 255==numbers[p]:
                           numberschangenotexist.append(notexist)
                    if lenfg==0:
                        byteb=numbers[p]
                        numberschangenotexist.append(byteb)
                    
                    #count 1789
                 
                  
                    
                    
                        
                    ghj=numberschangenotexist[p]
                    qfl=qfl+1
                    ghjd=ghj
                    bnk=1
                    bnks=1
                    bb=-1
                    bnkd=1
                       
                            
                    kl=kl-1
                    if qwa<=1:
                        while bb<kl:
                            if qwa<=1:
                                bb=bb+1
                            
                                
                            if qwa<=1:
                                bnk=bnk*255
                            
                               
                            if qwa<=1:
                                bnks=bnks*256
                      
                        
                                
                    if qwa<=1:
                        numberschangenotexistq.append(bnk)
                        numberschangenotexistqz.append(bnks)
                    if lenfg>0:
                        bnk=numberschangenotexistq[p]
                        ghjd=ghjd*bnk
                    if lenfg==0:
                        bnks=numberschangenotexistqz[p]
                        ghjd=ghjd*bnks
                    cvz=cvz+ghjd
                szx=bin(cvz)[2:]
                lenfa=len(szx)
                
                
               
                

                    
                    
                        
                       
                        
                           
                        
                    
                        
                        
                        
                if lenfa>14305:
                    wqwe=""
                    p=0
                    aaqq=""
                    d=1
                    a=0
                             
                    while p<2:
                                
                        aaqq=szx[a:d]
                                    
                        if aaqq=="1":
                            a=a+1
                            d=d+1
                            aaqq=str(aaqq)
                            aaqw=aaqw+aaqq
                        if aaqq=="0":
                            p=2
                            
                    aaqwss=len(aaqw)
                    aasqq=""
                    ass=0
                    asss=0
                            
                    ass=aaqwss

                    asss=aaqwss-1
                                
                                
                    aaad="0"
                    aasqq=szx[0:asss]
                    aasqq=str(aasqq)
                    szx=szx[d:]
                            
                           
                          
                    aaqw=""
                    zzaax=""
                    xc=14320-lenfa
                    z=0
                    if xc!=14320:
                        while z<xc:
                            zzaax="0"+zzaax
                            z=z+1
                    wer=wer+szx
                    aaqws=aaqws+zzaax+aasqq+"0"
                    szx=""    
                    zzaax=""
                    lenf=len(szx)
                    wqwe=""
                    wqwe=szx[0:1]
                    if wqwe=="1":
                        raise SystemExit   
                        
                if lenfa<=14305:
                    szx="0"+szx
                    xc=14306-lenfa
                    z=0
                    if xc!=14306:
                        while z<xc:
                            szx="1"+szx
                            z=z+1
                    wer=wer+szx
                    lenf=len(szx)
                    szx=""
                    notexist=k[0]
                    szx=bin(notexist)[2:]
                    lenf=len(szx)
                                
                    xc=8-lenf
                    z=0
                    while z<xc:
                        szx="0"+szx
                        z=z+1
                    wer=wer+szx
                    szx=""
                        
                
                
                a=0
                numberschangenotexist = []    
                del k[:]
                    
                del numbers[:]
                m = []
                b=0
                while b<1790:
                    m+=[-1]
                    b=b+1
                b=0
                b=0
                       
                        
            s=h%1790
        if s!=0:
            
            s=s-1
            p=-1
            if s!=1789:
                b=-1
                bb=0
                kl=s
                bnk=0
                cb=0
                er=0
                                   
                bb=-1
                cvz=0
                ghj=0
                ghjd=1
                bnk=1
                while p<s:
                    p=p+1
                    byteb=numbers[p]
                    numberschangenotexist.append(byteb)
                    
                            #count 1789
                  
                   
                        
                                  
                                    
                                        
                    
                    
                    
                                    
                    ghj=numberschangenotexist[b]         
                    ghjd=ghj
                    bnk=1
                    bb=-1
                    kl=kl-1
                    while bb<kl:
                        bb=bb+1
                        bnk=bnk*256
                    ghjd=ghjd*bnk
                    cvz=cvz+ghjd
                szx=bin(cvz)[2:]
                lenf=len(szx)
                
                   
                ert=0
                s=s+1
                ert=s*8
                    
               
                        
                szx=""
               
                        
                        
                 
                
        a=0
        szx=""
        
        
        
        dd=len(aaqws)
       
        xc=8-dd%8
        szxzz=""
        z=0
        if xc!=8:
            while z<xc:
                szxzz="0"+szxzz
                z=z+1
        
        dd=len(szx)
        
        
        xc=8-dd%8
        szxz=bin(dd)[2:]
        z=0
        if xc!=8:
            while z<xc:
                szxz="0"+szxz
                z=z+1
            
        dd=len(szxz)
        szxzz=""
        xc=8-dd%8
        szxzz=bin(dd)[2:]
        z=0
        if xc!=8:
            while z<xc:
                szxzz="0"+szxzz
                z=z+1
        
        wer="0b1"+wer+aaqws+"1"
        szx=""
        
        lenf=len(wer)
        xc=8-lenf%8
        z=0
        if xc!=8:
            while z<xc:
                szx="0"+szx
                z=z+1
        
        wer=wer+szx+szxzz+szxz+szxzz
        szx=""        
        n = int(wer, 2)
        jl=binascii.unhexlify('%x' % n)
            
        f2.write(jl)
        
             
            
        
  
           
