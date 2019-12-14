import os
import binascii
zzaax=""
szxzzzas=""
asaaq=""
assa=0
adwll1=0
ddf=0
cvz31=0
rw=0
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
        lenfaq=len(sda)
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
                bnks=byte*256*256*256
            if bb==2:
                bnks=byte*256*256
            if bb==3:
                bnks=byte*256
            if bb==4:
                bnks=byte
            cvz=cvz+bnks
        print(cvz)
                
        #start    
        rw=rw+1
        ddf=0
        if rw==1:
            ddf=4
        lenfaqd=lenf1-ddf
        lenfaqde=lenf1-1
        aaa=0
        
        for byte in data:
            sss=int(byte)
            aaa=aaa+1
            lenfq=lenf1-ddf
            if aaa==lenfq:
                adw=sss-10
            lenfq1=lenf1-ddf-1
            if aaa==lenfq1:
                llon8=sss
        print(adw)
        print("ok")
        print(llon8)
        print("ok")

        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        bbs=int(llon8/8)
        lenfq2=lenfq1-1
        lenfq3=lenfq2-bbs
        aqwe=data[lenfq3:lenfq2]
        for byte in aqwe:
            print(byte)
            print(bbs)
            if bbs>1:
                bnks=byte*(256**(bbs-1))
            if bbs==1:
                bnks=byte
                print(bnks)
                print("bnks")
                
            print(bbs)
                
            cvz3=cvz3+bnks
            print(cvz3)
            bbs=bbs-1
        print(cvz3)
        print("cvz3")
       

       
            

        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        zzz=""
        cvz31w=0
        adwll1e=8
        bbs=int(adwll1e)
        lenfq6=(lenfq3*8)-8
        lenfq7=lenfq6-bbs
        aqwes=sda[lenfq7:lenfq6]
        for byte in aqwes:
            print(byte)
            print(bbs)
            if bbs>1:
                zzz=zzz+byte
                if byte=="0":
                    byte=0
                if byte=="1":
                    byte=1
                bnks=byte*(2**(bbs-1))
                
            if bbs==1:
                zzz=zzz+byte
                if byte=="0":
                    byte=0
                if byte=="1":
                    byte=1
                bnks=byte
                
                print(bnks)
                print("bnks")
                
            print(bbs)
             
            cvz31w=cvz31w+bnks
            print(cvz31w)
            bbs=bbs-1
        
        print(cvz31w)
        print("ok")
        print(zzz)    

        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        zzz=""
        cvz31wl=0
        adwll1e=8
        bbs=int(adwll1e)
        lenfq7=lenfq7
        lenfq8=lenfq7-8
        aqwes=sda[lenfq8:lenfq7]
        for byte in aqwes:
            print(byte)
            print(bbs)
            if bbs>1:
                zzz=zzz+byte
                if byte=="0":
                    byte=0
                if byte=="1":
                    byte=1
                bnks=byte*(2**(bbs-1))
                
            if bbs==1:
                zzz=zzz+byte
                if byte=="0":
                    byte=0
                if byte=="1":
                    byte=1
                bnks=byte
                
                print(bnks)
                print("bnks")
                
            print(bbs)
             
            cvz31wl=cvz31wl+bnks
            print(cvz31wl)
            bbs=bbs-1
        
        print(cvz31wl)
        print("ok")
        print(zzz)
        cvz31wl=cvz31wl-10
        print(cvz31wl)
           
          
        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        zzz=""
        bbs=int(cvz31wl)
        lenfq9=lenfq8
        lenfq10=lenfq9-bbs
        aqwes=sda[lenfq10:lenfq9]
        bitcut=""
        for byte in aqwes:
            bitcut=bitcut+byte
        print(bitcut)

        
        bnks=0
        ghjd=0
        kl=3
        cvz3=0
        zzz=""
        bbs=int(cvz31wl)
        lenfq11=lenfq10
        qqwww3=add
        lenfq12=0+(qqwww3*8)+8
        aqwes=sda[lenfq12:lenfq11]
        bitcutake=""
        for byte in aqwes:
            bitcutake=bitcutake+byte
        print(bitcutake)     
                
   
if namez=="c":
    name = input("What is name of file? ")
    namea="file.Spring"
    namem=name+"/"
    namema="?"
    namemas="<"
    blockw=4
    blockw1=3
    
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

        if lenf1==0:
            jlz=""
            f2.write(jlz)
            raise SystemExit
        if lenf1<6:
            print("This file is too small");
            raise SystemExit
        if lenf1>2**256:
            print("This file is too big");
            raise SystemExit

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
            assa=0
            asaaq=""
            szxzzzas=""
            s=""
            blockw=blockw+1
            blockw1=blockw1+1
            sdaa=""
            aas=0
            asaaq=""
            #print(blockw)
            
           
            with open(namea, "ab") as f2:
                sda=bin(int(binascii.hexlify(data),16))[2:]
                lenf=len(sda)
                xc=(lenf1*8)-lenf
                z=0
                if xc!=0:
                    while z<xc:
                        sda="0"+sda
                        z=z+1
                      
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
                        assa=assa+1
                        qqw1q="0"
                        
                        if blockw==5:
                            
                            if szxx=="0000000000000000000000000000000000000000":
                                qqw1q="10"
                                

                                szxzzzas=""
                                szxzzzas=bin(assa)[2:]
                                dd=len(szxzzzas)
                                xc=8-dd%8
                                z=0
                                if xc!=0:
                                    while z<xc:
                                        szxzzzas="10"+szxzzzas
                                        z=z+1
                                        
                                dd=len(szxzzzas)
                                szxzzzasaa=""
                                szxzzzasaa=bin(dd)[2:]
                                dd=len(szxzzzasaa)
                                xc=8-dd%8
                                z=0
                                if xc!=0:
                                    while z<xc:
                                        szxzzzasaa=""+szxzzzasaa
                                        z=z+1
                                
                                
                                asaaq=asaaq+szxzzzas+szxzzzasaa
                                #print(asaaq)
                                
 				
                                
                            if szxx=="1111111111111111111111111111111111111111":    
                                qqw1q="11"
                               
                                szxzzzas=""
                                szxzzzas=bin(assa)[2:]
                                dd=len(szxzzzas)
                                xc=8-dd%8
                                z=0
                                if xc!=0:
                                    while z<xc:
                                        szxzzzas="11"+szxzzzas
                                        z=z+1
                                
                                dd=len(szxzzzas)
                                szxzzzasaa=""
                                szxzzzasaa=bin(dd)[2:]
                                dd=len(szxzzzasaa)
                                xc=8-dd%8
                                z=0
                                if xc!=0:
                                    while z<xc:
                                        szxzzzasaa=""+szxzzzasaa
                                        z=z+1
                                
                                
                                asaaq=asaaq+szxzzzas+szxzzzasaa
                                
                                
 			        
                                        
                            
                            
                        if qqw1q=="0":
                            d=1
                            a=0
                            while p<1:
                                         
                                aaqql=szxx[a:d]
                                                
                                if aaqql=="0":
                                        
                                    a=a+1
                                    d=d+1
                                if aaqql=="1":
                                    p=p+1
                            szx=szxx[a:]
                            
                            lenfa=len(szx)
                                
                            
                                
                            if lenfa>=((blockw*8)-5):
                                szx=szx[1:]
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
                                
                                
                                
                                szxza=""
                                da=0
                                qqw1=0
                                xc=(blockw*8)-lenfa
                                
                                z=0
                                
                                    
                                    
                                
                                xc=(blockw*8)-lenfa
                                z=0
                                if xc!=(blockw*8):
                                    while z<xc:
                                            
                                        
                                        
                                        zzaax="0"+zzaax
                                        zzaax1="1"+zzaax1
                                        z=z+1
                                    
                                    
                                
                                wer=wer+szx
                                
                               
                                
                                
                                zzaax="1"+zzaax
                                
                            
                                
                                fffgjv=fffgjv+aaaq
                                fffgjv1=fffgjv1+aaaq1
                                
                                
                                
                                aaqws=aaqws+fffgjv
                                
                                
                                fffgjv=""
                                
                                
                                
                                
                                fffgjv1=""
                                  
                                
                                lenf=len(szx)
                                wqwe=""
                                wqwe=szxza[0:1]
                                 
                                    
                            if lenfa<=((blockw*8)-6):
                                 
                                
                                szx=szx[1:]
                                
                                aqqd1=len(zzaax1)
                                
                                
                                
                               
                                xc=((blockw*8)-5)-lenfa
                                z=0
                                szx="0"+szx
                                if xc!=((blockw*8)-5):
                                    while z<xc:
                                        szx="1"+szx
                                        z=z+1
                                if aqqd1==0:
                                    szx=szx+""
                                else:
                                    szx=szx
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
                        aqqd1=len(zzaax1)
                        if aqqd1==0:
                            szx=szx+""
                        else:
                            szx=szx
                        szx=szx+""
                        szx=""+szx
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
                
                
                
                
                dd=len(aaqws)
                dda=len(zzaax)


                ddwa=len(asaaq)
                
                szxzzzq=""
                szxzzzq=bin(ddwa)[2:]
                ddwa=len(szxzzzq)
                xc=8-ddwa%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzzzq="0"+szxzzzq
                        z=z+1
                
                ddwa=len(szxzzzq)


                szxzzzqq=""
                szxzzzqq=bin(ddwa)[2:]
                ddwa=len(szxzzzqq)
                xc=8-ddwa%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzzzqq="0"+szxzzzqq
                        z=z+1
                
                dd=len(szxzzzqq)

                szxzzzqqz=""
                szxzzzqqz=bin(dd)[2:]
                ddwa=len(szxzzzqqz)
                xc=8-ddwa%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzzzqqz="0"+szxzzzqqz
                        z=z+1

                dd=len(szxzzzqqz)

               
                
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

                szxzzza=""
                szxzzza=bin(dda)[2:]
                dda=len(szxzzza)
                xc=8-dda%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzzza="0"+szxzzza
                        z=z+1
                
                dda=len(szxzzza)

                szxz=""
                szxz=bin(dda)[2:]
                dda=len(szxz)
                xc=8-dda%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxz="0"+szxzs
                        z=z+1
                        
                dda=len(szxz)
                szxzff=""
                szxzff=bin(dda)[2:]
                dda=len(szxzff)
                xc=8-dda%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzff="0"+szxzff
                        z=z+1

                


                
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

                szxzas=""
                szxzas=bin(dd)[2:]
                dda=len(szxzas)
                xc=8-dda%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzas="0"+szxzas
                        z=z+1

                
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
                
                aqqd1=len(zzaax)
                
                szxzzz=""
                szxzzz=bin(aqqd1)[2:]
                dd=len(szxzzz)
                xc=8-dd%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzzz="0"+szxzzz
                        z=z+1
                
                dd=len(szxzzz)
               
                if aqqd1>0:
                    wer="1"+wer+aaqws+zzaax+asaaq+"1"
                else:
                    wer="1"+wer+aaqws+zzaax+asaaq+"1"
                zzaax=""
                    
                
                
                aqqwwa=10    
                lenf=len(wer)
                xc=8-lenf%8
                z=0
                if xc!=0:
                    while z<xc:
                        szx="0"+szx
                        z=z+1
                        aqqwwa=aqqwwa+1
                szxzlz=""
                
                szxzlz=bin(aqqww)[2:]
                dds=len(szxzlz)
                xc=8-dds%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzlz="0"+szxzlz
                        z=z+1


                szxzlz1=bin(aqqwwa)[2:]
                dds=len(szxzlz1)
                xc=8-dds%8
                z=0
                if xc!=0:
                    while z<xc:
                        szxzlz1="0"+szxzlz1
                        z=z+1
                        
                wer=wer+szx+szxzlz1+szxzzz+szxz+szxzas+szxzc+szxzl+szxzlz+szxzzza+szxzs+szxzff+szxzzzq+szxzzzqq+szxzzzqqz
                szx=""
                
                n = int(wer, 2)
                jl=binascii.unhexlify('%x' % n)
                data=jl
                sssssw=len(jl)
                qqqwz=qqqwz+1
                szxzzza=""
                szxzs=""
               
                
                blockw=4
                blockw1=3
                
                #print(sssssw)
                    
                saaq=0
                if lenf1<=sssssw and qqqwz==1:
                    saaq=1
                
                    
                if lenf1<=sssssw and saaq==0 and qqqwz==2**256 or sssssw<=1400 or qqqwz==2**256:
                    szxzzzqqax=""
                    szxzzzqqax=bin(qqqwz)[2:]
                    dd=len(szxzzzqqax)
                    xc=8-dd%8
                    z=0
                    if xc!=0:
                        while z<xc:
                            szxzzzqqax="0"+szxzzzqqax
                            z=z+1
                    
                    dd=len(szxzzzqqax)
                    szxzzzqq=""
                    szxzzzqq=bin(dd)[2:]
                    dd=len(szxzzzqq)
                    xc=8-dd%8
                    z=0
                    if xc!=0:
                        while z<xc:
                            szxzzzqq="0"+szxzzzqq
                            z=z+1
                    zsaqq=""
                    zsaqq=zsaqq+szxzzzqqax+szxzzzqq 
                    
                    
                    szx=""
                    wer=wer+zsaqq
                
                    n = int(wer, 2)
                    
                    jlz=binascii.unhexlify('%x' % n)
                    
                    assx=10
                    if assx==10:
                        f2.write(jlz)
                    
                     
                    
                
          
                   
