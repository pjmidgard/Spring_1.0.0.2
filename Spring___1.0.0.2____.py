import binascii
import json
name = input("What is name of file? ")
qwert=0
asj=0
qwtl=0
dfq=0
cvzj=0
asjx=0

cvz=0
cvqz=0

while qwert<2:
    
    qwert=qwert+1
    a=0
    b=0
    
    cvqwz=0
    cvzq=0
    ghjdq=0
    asdft=0
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
    asd=""
    b=0
    
    aaqw=""
    aqwret=0
    szx=""
    asf2="0b"
    while b<1524:
        m+=[-1]
        b=b+1
    k = []
    wer=""
    numberschangenotexist = []
    numbers = []
    
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
        with open(namea, "ab") as f2:
            for byte in data:
                av=bin(byte)
                a=a+1
                if a<=1524:
                    byte=int(byte)
                    m[byte] = byte
                    numbers.append(byte)
                    h=h+1
                    if qwert==1:
                        qwtl=qwtl+1
                    
                if a == 1524:
                    
                    p=0
                    while p<256:
                        if p!=m[p]:
                            k.append(p)
                            
                        p=p+1
                    
                    #lenf count
                    lenfg=len(k)
                    
                    

                    if lenfg>0:
                        notexist=k[0]
                        szx=bin(notexist)[2:]
                        
                        
                       
                    
                        
                    b=-1
                    bb=0
                    kl=1523
                    bnk=0
                    cb=0
                    ghjdd=1
                    
                    cvzl=0       
                    bb=-1
                    er=-1
                    ghj=0
                    ghjd=1
                    bnk=1
                    p=-1
                    cvz=0
                    qwa=qwa+1
                    while p<1523:
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
                        
                        #count 1523
                     
                      
                        
                        
                            
                        ghj=numberschangenotexist[p]
                        qfl=qfl+1
                        
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
                            
                            ghjd=ghj*bnk
                            if qwa<=1:
                                bnk=numberschangenotexistq[p]
                                ghjdq=254*bnk

                            
                        if lenfg==0:
                            bnks=numberschangenotexistqz[p]
                            
                            ghjdd=ghj*bnks

                            if qwa<=1:
                                bnk=numberschangenotexistq[p]
                                ghjdq=254*bnk
                        if qwa<=1:    
                            cvzq=cvzq+ghjdq
                        
                        cvz=cvz+ghjd
                        cvzl=cvzl+ghjdd
                        
                            
                        
                            
                   

                    
                    
                   
                    if lenfg>0:
                        szx=bin(cvz)[2:]
                        lenf=len(szx)
                        xc=12183-lenf
                        z=0
                        if xc!=0:
                            while z<xc:
                                szx="0"+szx
                                z=z+1
                        wer=wer+szx
                        lenf=len(szx)
                        if qwert==1:
                            aaqwq=szx[0:12182]
                            cvz=int(aaqwq,2)
                        
                            if cvqwz<cvz:
                                dfq=cvz
                                asj=qwtl
                        if qwert==1:
                            cvqwz=cvz
                            asjx=qwtl

                        szx=""

                        notexist=k[0]
                        szx=bin(notexist)[2:]
                        lenf=len(szx)
                        xc=8-lenf
                        z=0
                        if xc!=0:
                            while z<xc:
                                szx="0"+szx
                                z=z+1
                        wer=wer+szx
                        lenf=len(szx)
                        
                        szx=""
                        
                    if lenfg==0:
                        szx=bin(cvzl)[2:]
                        lenf=len(szx)
                        xc=12192-lenf
                        aaqw=szx[0:12182]
                        z=0
                        if xc!=0:
                            while z<xc:
                                szx="0"+szx
                                z=z+1
                        wer=wer+szx
                        lenf=len(szx)
                        if qwert==2:
                            
                            aqwret=int(aaqw,2)
                            
                            
                            if aqwret>cvqwz:
                                asdft=1
                            if aqwret<=cvqwz:
                                asdft=0
                                raise SystemExit
                        
                        szx=""
                    
               
                    a=0
                    numberschangenotexist = []    
                    del k[:]
                        
                    del numbers[:]
                    m = []
                    b=0
                    while b<1524:
                        m+=[-1]
                        b=b+1
                    b=0
                    b=0
                           
                            
                s=h%1524
            if s!=0:
                
                s=s-1
                p=-1
                if s!=1523:
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
                        ghjd=0
                        ghjd=ghj*bnk
                        cvz=cvz+ghjd
                    szx=bin(cvz)[2:]
                    lenf=len(szx)
                       
                    ert=0
                    s=s+1
                    ert=s*8
                        
                    xc=ert-lenf
                    z=0
                    if xc!=ert:
                        while z<xc:
                            szx="0"+szx
                            z=z+1
                        wer=wer+szx
                        lenf=len(szx)
                            
                        szx=""
                   
                       
                    szx=bin(asj)[2:]
                    lenf=len(szx)
                    xc=32-lenf
                    z=0
                    if xc!=0:
                        while z<xc:
                            szx="0"+szx
                            z=z+1
                        wer=wer+szx
                        lenf=len(szx)
                            
                        szx=""

                    szx=bin(asjx)[2:]
                    lenf=len(szx)
                    xc=32-lenf
                    z=0
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
            if qwert==1:
                jl=""
            if qwert==2:
                f2.write(jl)
            
                 
                
            
      
               
