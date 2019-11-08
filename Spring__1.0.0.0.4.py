import os
import binascii
qqw1q=""
lenfzzz=0
fffgjv=""
fffgjv1=""
zzaax1=""
qqqs=0
a=0
blockw=5
blockw1=4
cvb=0
zsaqq=""
qqqwz=0
assx=0
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
add=0
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
namez = input("c for compress u for unpack? ")
if namez=="u":
    name = input("What is name of file? ")
    namea="file.Spring"
    namem=name+"/"
    namema="?"
    namemas="<"
    with open(name, "rb") as binary_file:
        # Read the whole file at once
        data = binary_file.read()
        s=str(data)
        
        lenf1=len(data)
        szx=""
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
            
            adda=0
            asss=0
            add=0
            qwss=""
            for byte in data:
                
               
                if byte==47:
                    asss=1
                    
                    
                    
                if asss==0:
                    add=add+1
            saqqraz=byte
            aqwe1=""
            zaaqa=0
            zaaqaz=0
            zaaqa=lenf1-2
            zaaqaz=lenf1-1
            aqwe1=data[zaaqa:zaaqaz]
            aaa1=""        
            print(add)
            with open(name, "rb") as za:     
                dataa = za.read()
            add=add
            sss1=add-2
            aaa1=dataa[0:add]
            print(aaa1)
            aaa2=aaa1.decode("utf-8")
            print(aaa2)
            s=""
            with open(aaa2, "w") as f11:
                f11.write(s)

            #start
            cvz=0
            lenf1=len(data)
            zaaq=lenf1-4
            aqwe=""
           
            szx=""
            bnks=0
            ghjd=0
            kl=3
            bb=0
            lenfw1=lenf1-5
            lenfw=lenf1-4
            aqwe=data[zaaq:lenf1]
            for byte in aqwe:
                print(byte)
                bb=bb+1
                if bb==1:
                    bnks=byte
                if bb==2:
                    bnks=byte*256*256
                if bb==3:
                    bnks=byte*256
                if bb==4:
                    bnks=byte
                cvz=cvz+bnks
            print(cvz)
            cvz1=0
            aqwe=data[lenfw1:lenfw]
            for byte in aqwe:
                print(byte)
                
                cvz1=byte
            print(cvz1)
            bb=cvz1/8
            print(bb)
            
            bba=int(bb)
            bbs=int(bb)
            bnks=0
            ghjd=0
            kl=3
            cvz3=0
            lenfw=lenfw-1
            lenfw1=lenfw1-bba
            aqwe=data[lenfw1:lenfw]
            for byte in aqwe:
                print(byte)
                print(bbs)
                if bbs>1:
                    bnks=byte*((bbs-1)*256)
                if bbs==1:
                    bnks=byte
                    print(bnks)
                    print("bnks")
                
                print(bbs)
                
                cvz3=cvz3+bnks
                print(cvz3)
                bbs=bbs-1
            print(cvz3)
            
            
           
          

                
   
if namez=="c":
    name = input("What is name of file? ")
    namea="file.Spring"
    namem=name+"/"
    namema="?"
    namemas="<"
    blockw=5
    blockw1=4
    
    s=""
    if name=="file.Angel":
        with open(namea, "w") as f4:
                f4.write(s)
        with open(namea, "a") as f3:
                f3.write(namemas)
    elif name=="filea.Spring":
        with open(namea, "w") as f4:
                f4.write(s)
        with open(namea, "a") as f3:
                f3.write(namema)
    else:    
        with open(namea, "w") as f4:
                f4.write(s)
        with open(namea, "a") as f3:
                f3.write(namem)
    with open(name, "rb") as binary_file:
        # Read the whole file at once
        data = binary_file.read()
        s=str(data)
        lenf1=len(data)

        while assx<10:
            if qqqwz>1:
                lenf1=sssssw
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
            
            s=""
            blockw=blockw+1
            blockw1=blockw1+1
            sdaa=""
            aas=0
            if lenf1<20:
                print("This file is too small");
                raise SystemExit
            with open(namea, "ab") as f2:
                sda=bin(int(binascii.hexlify(data),16))[2:]
                for byte in sda:
                    sda=str(sda)
                    sdaa=sdaa+byte
                  
                    aas=aas+1
                    if aas==8:
                        a=a+1
                        aas=0
                    
                    if a == blockw:
                        szxx=""
                        szxx=sdaa
             
                        wqwe=""
                        p=0
                        aaqq=""
                        d=1
                        a=0
                        da=0
                        aaqw=""
                        aaqql=""

                        qqw1q="0"
                        
                        if szxx=="000000000000000000000000000000000000000000000000":
                            qqw1q="10"   
                        if szxx=="111111111111111111111111111111111111111111111111":    
                            qqw1q="11"

                        if qqw1q=="0":
                            
                            while p<1:
                                            
                                aaqql=szxx[a:d]
                                                
                                if aaqql=="0":
                                        
                                    a=a+1
                                    d=d+1
                                if aaqql=="1":
                                    p=p+1
                            szx=szxx[a:]
                            
                            lenfa=len(szx)
                                
                            
                                
                            if lenfa>=((blockw*8)-2):
                                wer=wer+"00"
                                wqwe=""
                                p=0
                                aaqq=""
                                d=1
                                a=0
                                da=0
                                aaqw=""
                                aaqw1=""
                                fffgjv=""
                                fffgjv1=""
                                while p<1:
                                            
                                    aaqq=szx[a:d]
                                                
                                    if aaqq=="1":
                                        da=da+1
                                        if da==1:
                                            a=a+1
                                            d=d+1
                                            aaqq=str(aaqq)
                                            aaqw=aaqw+"0"
                                            aaqw1=aaqw1+"1"
                                        else:
                                            a=a+1
                                            d=d+1
                                            aaqq=str(aaqq)
                                            aaqw=aaqw+aaqq
                                            aaqw1=aaqw1+"0"
                                    if aaqq=="0":
                                        p=p+1
                                aaaq1=""
                                aaaq=""
                                aaaq=aaqw
                                aaaq1=aaqw1 
                                aaqwss=len(aaqw)
                                aasqq=""
                                ass=0
                                asss=0
                                        
                                ass=aaqwss

                                asss=aaqwss-1
                                            
                                d=d-1       
                                aaad="0"
                                
                           
                                szx=szx[d:]
                                
                                       
                                szzs=0
                                
                                zzaax=""
                                
                                szxza=""
                                da=0
                                qqw1=0
                                xc=(blockw*8)-lenfa
                                z=0
                                if xc!=(blockw*8):
                                    while z<xc:
                                            
                                        
                                        
                                        zzaax="0"+zzaax
                                        zzaax1="1"+zzaax1
                                        z=z+1
                                    
                                    
                                
                                wer=wer+szx+zzaax
                                
                               
                                
                                
                                zzaax1="0"+zzaax1
                                
                            
                                
                                fffgjv=fffgjv+aaaq
                                fffgjv1=fffgjv1+aaaq1
                                
                                
                                
                                aaqws=aaqws+fffgjv
                                
                                
                                fffgjv=""
                                
                                
                                
                                
                                fffgjv1=""
                                  
                                
                                lenf=len(szx)
                                wqwe=""
                                wqwe=szxza[0:1]
                                 
                                    
                            if lenfa<=((blockw*8)-6):
                                wer=wer+"01"
                                if lenfa==0:
                                    lenfa=1
                                    szx="0"+szx
                                szx=szx[1:]
                                szx="0"+szx
                                aqqd1=len(zzaax1)
                                
                                szx=zzaax1+szx
                                if aqqd1==0:
                                    szx="0"+szx
                                else:
                                    szx=zzaax1+szx
                                szx="0"+szx
                                xc=((blockw*8)-5)-lenfa
                                z=0
                                if xc!=((blockw*8)-5):
                                    while z<xc:
                                        szx="1"+szx
                                        z=z+1
                                
                                asss1=len(szx)
                                asss2=asss1-1
                                qqw=szx[asss2]
                                if qqw=="1":
                                    szx=szx
                                if qqw=="0":
                                    szx=szx
                                    
                                wer=wer+szx
                                lenf=len(szx)
                                szx=""
                                fffgjv1=""
                                fffgjv=""
                                zzaax1=""
                                
                                lenf=len(szx)
                                szx=""
                        
                        else:
                            wer=wer+qqw1q
                            
                        zzaax=""
                        
                        
                        sdaa=""
                        a=0
                        numberschangenotexist = []    
                        del k[:]
                            
                        del numbers[:]
                        m = []
                        b=0
                        while b<blockw:
                            m+=[-1]
                            b=b+1
                        b=0
                        b=0
                               
                                
                    s=a%blockw
                    
                if s!=0:
                    
                    s=s-1
                    p=-1
                    if s!=blockw1:
                        
                        szx=sdaa
                        szx="10"+szx
                        aqqd1=len(zzaax1)
                        if aqqd1==0:
                            szx="0"+szx
                        else:
                            szx=zzaax1+szx
                        szx="0"+szx
                        asss1=len(szx)
                        asss2=asss1-1
                        qqw=szx[asss2]
                        if qqw=="1":
                            szx=szx
                        if qqw=="0":
                            szx=szx
                        wer=wer+szx
                        lenfzzz=len(szx)
                        szx=""
                        fffgjv1=""
                        fffgjv=""
                            
                        lenf=len(szx)
                        szx=""
                        zzaax1=""        
                         
                        
                a=0
                szx=""
                
                
                wer+wer+zzaax1+"0"
                
                dd=len(aaqws)
                
                
                szxzzz=""
                szxzzz=bin(dd)[2:]
                dd=len(szxzzz)
                xc=8-dd%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzzz="0"+szxzzz
                        z=z+1
                
                dd=len(szxzzz)
                
                
                szxz=""
                szxz=bin(dd)[2:]
                dd=len(szxz)
                xc=8-dd%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxz="0"+szxz
                        z=z+1
                        
                dd=len(szxz)
                szxzz=""
                szxzc=""
                szxzc=bin(lenfzzz)[2:]
                dd=len(szxzc)
                xc=8-dd%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzc="0"+szxzc
                        z=z+1
                        
                dd=len(szxzc)
                szxzz=""

                aqqww=10
                szxzl=""
                szxzl=bin(dd)[2:]
                dd=len(szxzl)
                xc=8-dd%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzl="0"+szxzl
                        aqqww=aqqww+1
                        z=z+1
                
                aqqd1=len(zzaax1)
                
                if aqqd1>0:
                    wer="1"+wer+aaqws+"10"
                else:
                    wer="1"+wer+aaqws+"11"
                    
                
                
                    
                lenf=len(wer)
                xc=8-lenf%8
                z=0
                if xc!=0:
                    while z<xc:
                        szx="0"+szx
                        z=z+1

                szxzlz=""
                
                szxzlz=bin(aqqww)[2:]
                dds=len(szxzlz)
                xc=8-dds%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzlz="0"+szxzlz
                        z=z+1
               
                wer=wer+szx+szxzzz+szxz+szxzc+szxzl+szxzlz
                szx=""
                
                n = int(wer, 2)
                jl=binascii.unhexlify('%x' % n)
                data=jl
                sssssw=len(jl)
                qqqwz=qqqwz+1
               
                #print(sssssw)
                if blockw==6:
                   blockw=5
                   blockw1=4
                if lenf1<=sssssw or sssssw<=20 or qqqwz==2**30:
                    
                    szx=bin(qqqwz)[2:]
                    lenf=len(szx)
                    xc=32-lenf%32
                    z=0
                    if xc!=0:
                        while z<xc:
                            szx="0"+szx
                            z=z+1
                    zsaqq=zsaqq+szx
                    
                    szx=""
                    wer=wer+zsaqq
                
                    n = int(wer, 2)
                    
                    jlz=binascii.unhexlify('%x' % n)
                    
                    assx=10
                    if assx==10:
                        f2.write(jlz)
                    
                     
                    
                
          
                   
