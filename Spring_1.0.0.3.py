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

    szxz=""
    lenfa=0
    block=1
    blockw=0
    blockw1=1
    virationc=1
    asqw=0
    bitc=32
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
    zxvbf=0

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
    while dd<1:

        zxvbf=0
        szxz=""
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
        asqw=0
        
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
           
            if aqwer<=bitc:
                qwt=qwt+byte
            if aqwer==bitc:
                aqwq=int(qwt,2)
                qwt=""
                a=a+1
                h=h+1
                asqw=asqw+1
            
            
                
            av=bin(aqwq)
            if a<=block and aqwer==bitc:
                aqwer=0

            if a == block:
                
                p=0
                
                
                 
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
                szxv=bin(asqw)[2:]
                lenfqw=len(szxv)
                szx=bin(aqwqs)[3:]
                cvz=0
                lenf=len(szx)
                lenfb=len(szxv)
                

                
                
                                 
                if aqwqs==0:
                    raise SystemExit
                
                if lenf==31:
                       
                    xc=31-lenf%31
                    z=0
                    
                    if xc!=0:
                        if xc!=31:
                            while z<xc:
                                szx="1"+szx
                                z=z+1
                    szx="0"+szx
                    wer=wer+szx
                    lenfd=len(szx)
                    szx=""

                if lenf==30:
                        
                    xc=30-lenf%30
                    z=0
        
                    if xc!=0:
                        if xc!=30:
                            while z<xc:
                                szx="1"+szx
                                z=z+1
                    szx="10"+szx
                    wer=wer+szx
                    
                    
                    szx=""

                if lenf<=29:
                        
                    xc=29-lenf%29
                    z=0
        
                    if xc!=0:
                        if xc!=29:
                            while z<xc:
                                szx="1"+szx
                                z=z+1
                    szx="11"+szx
                    wer=wer+szx
                    
                
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
    
        wer="0b"+wer
        n = int(wer, 2)
        jl=binascii.unhexlify('%x' % n)
        data=jl
    with open(namea, "ab") as f2ww:             
        f2ww.write(jl)        
            
                    
                         
                        
                    
              
                       
