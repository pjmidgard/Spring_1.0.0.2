import os
import binascii
fffgjv=""
fffgjv1=""
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
        zaaq=lenf1-1
        aqwe=""
       
        szx=""
        
        aqwe=data[zaaq:lenf1]
        for byte in aqwe:
            print(byte)
      
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
                            
                            wqwe=""
                            p=0
                            aaqq=""
                            d=1
                            a=0
                            da=0
                            aaqw=""
                            aaqw1=""
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
                            zzaax1=""
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
                                
                                
                          
                            wer=wer+szx
                            
                           
                            
                            
                            zzaax1="01"+zzaax1
                            
                            
                            fffgjv=fffgjv1+aaaq
                            fffgjv1=fffgjv1+aaaq1
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            fffgjv=""
                              
                            
                            lenf=len(szx)
                            wqwe=""
                            wqwe=szxza[0:1]
                            if wqwe=="1":
                                raise SystemExit
                            zzaax=""
                            szx=""  
                                
                        if lenfa<=((blockw*8)-6):
                            szx=szx[1:]
                            szx="0"+szx
                            szx=zzaax1+szx
                            szx="0"+szx
                            xc=((blockw*8)-2)-lenfa
                            z=0
                            if xc!=((blockw*8)-2):
                                while z<xc:
                                    szx="1"+szx
                                    z=z+1
                            
                            asss1=len(szx)
                            asss2=asss1-1
                            qqw=szx[asss2]
                            if qqw=="1":
                                szx=szx+fffgjv
                            if qqw=="0":
                                szx=szx+fffgjv1
                            wer=wer+szx
                            lenf=len(szx)
                            szx=""
                            fffgjv1=""
                            fffgjv=""
                            
                            lenf=len(szx)
                            szx=""
                        
                            
                        zzaax=""
                        zzaax1=""    
                        
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
                        asss1=len(szx)
                        asss2=asss1-1
                        qqw=szx[asss2]
                        if qqw=="1":
                            szx=szx+fffgjv
                        if qqw=="0":
                            szx=szx+fffgjv1
                        wer=wer+szx
                        lenf=len(szx)
                        szx=""
                        fffgjv1=""
                        fffgjv=""
                            
                        lenf=len(szx)
                        szx=""
                                
                         
                        
                a=0
                szx=""
                
                
                
                
                aasd=len(fffgjv)
                if aasd>0:
                    raise SystemExit
                wer="1"+wer+"1"
                lenf=len(wer)
                xc=8-lenf%8
                z=0
                if xc!=0:
                    while z<xc:
                        szx="0"+szx
                        z=z+1
               
                wer=wer+szx
                szx=""
                aaqws=""
                n = int(wer, 2)
                jl=binascii.unhexlify('%x' % n)
                if qqqs==0:
                    data=jl
                sssssw=len(jl)
                qqqwz=qqqwz+1
               
               
                if blockw==6:
                   blockw=5
                   blockw1=4
                if lenf1<=sssssw or sssssw<=20 or qqqwz==1:
                    
                 
                    assx=10
                    if assx==10:
                        f2.write(jl)
                   
                
                     
                    
                
          
                   
