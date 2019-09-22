import os
from multiprocessing import Pool,Value

def f(x):
    
    return 16383**(x+1)

if __name__ == '__main__':
    pool = Pool(processes=4)               # start 4 worker processes
    #result = pool.apply_async(f, [147456])     # evaluate "f(10)" asynchronously
    #print(result.get(timeout=1))           # prints "100" unless your computer is *very* slow
    #print(pool.map(f, range(147456)))          # prints "[0, 1, 4,..., 81]"
    
    
   

    import binascii
    import json


    lenfa=0
    block=1
    blockw=0
    blockw1=1
    virationc=1
    asqw=0
    bitc=4
    lenf1=0
    a=0
    qfl=0
    h=0
    byteb=""
    notexist=""
    lenf=0
    dd=0
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
    namem=name+"+"
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
        
        if lenf1<100:
            print("This file is too small");
            raise SystemExit
        s=str(data)
        lenf=len(data)
    while dd<10:


        lenfa=0
        a=0
        qfl=0
        h=0
        byteb=""
        notexist=""
        lenf=0
       
        numberschangenotexistq = []
        
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
        s=""
        qwt=""
        ert=0
        aqwer=0
        aqwq=0
        aqwers=0
        qwaw=""
        dd=dd+1
        szx=""
        if dd==1:
            sda=bin(int(binascii.hexlify(data),16))[2:]
        
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
            asqw=asqw+1
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

            if a == block:
                
                p=0
                
                
                lenfg=1
                if lenfg==0:
                    raise SystemExit
                b=-1
                kl=blockw
                cb=0        
                er=-1
                ghj=0
                ghjd=1
                bnk=1
                p=0
                cvz=0
                aqwqs=0
                qwa=qwa+1
                aqwqs=int(qwaw,2)
                szxv=""
                szxv=bin(aqwqs)[2:]
                szx=bin(aqwqs)[3:]
                cvz=0
                lenf=len(szx)
                lenfb=len(szxv)
                szx=""
                
                if szxv=="0000":
                        
                    szx="0000"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""


                if szxv=="0001":
                        
                    szxz=szxv+szxz
                    lenfa=asqw  
                    szx=""
                if asqw==16 and lenfa!=0:

                    wer=wer+szxz
                    szxz=""
                    asqw==0

                if asqw==16 and lenfa==0:

                    wer=wer+"0000"
                    szxz=""
                    asqw==0
                    
                if szxv=="0010":
                        
                    szx="100"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""

                if szxv=="0011":
                        
                    szx="101"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""

                if szxv=="0100":
                        
                    szx="1100"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""
                    
                if szxv=="0101":
                        
                    szx="1101"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""

                if szxv=="0110":
                        
                    szx="1110"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""
                    
                if szxv=="0111":
                        
                    szx="1111"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""

                if szxv=="1000":
                        
                    szx="1000"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""

                if szxv=="1001":
                        
                    szx="0001"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""
                    
                if szxv=="1010":
                        
                    szx="0010"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""

                if szxv=="1011":
                        
                    szx="0011"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""
                    
                if szxv=="1100":
                        
                    szx="0100"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""

                if szxv=="1101":
                        
                    szx="0101"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""

                if szxv=="1110":
                        
                    szx="0110"+szx
                    wer=wer+szx
                    lenf=len(szx)  
                    szx=""

                if szxv=="1111":
                        
                    szx="0111"+szx
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
                qwaw=""
                
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
        if dd==10:
            wer="0b"+wer
            n = int(wer, 2)
            jl=binascii.unhexlify('%x' % n)
        sda=wer
    with open(namea, "ab") as f2ww:             
        f2ww.write(jl)        
            
                    
                         
                        
                    
              
                       
