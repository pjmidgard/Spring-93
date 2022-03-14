from time import time
cvf=0
import os
import binascii
import math
import os.path

lenf=0
name=""
szx=""
wer=""

namez = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:
       
        def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas"

                if namez!="c" and namez!="e":
                        print("The wrong letter")
                        raise SystemExit
                if namez=="c" or namez=="e":        
                    if namez=="c":


                        i=1

                    if namez=="e":
                        i=2
                 
                    sda4=""
                    sda5=""
                    sda6=""
                    Corrupted=0
                      
                    name = input("What is name of file? ")

                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                            
                    
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)
                    
                    ccc=1

                    if i==2:
                        if nameas[nac-4:nac]==".bin":
                   
                        	nameas=name[:nac-4]
                        	nac=len(nameas)
                        	
                        	C=1

                        elif nameas[nac-4:nac]!=".bin":
                                print("Sorry, this is not binary file!")
                                raise SystemExit
                   
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    	
                    nac=len(nameas)
                    
                    Circle_times3=0
                    cvf=2
                    cvf1=0
                    s=""

                    sda3=""
                    sda2=""

                    sda5=""
                    sda6=""

                    sda11=""

                    D=0

                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        if lenf7==0:
                        	 raise SystemExit
                        
                        END_working=0
                        Circle_times2=0
                                   
                        sda23=""
 
                        sda18=""
                        sda29=""
                        
                        SpinS=0
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1
                            D=1
                            if D==1:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if Circle_times3==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**40)-1:
                                        raise SystemExit

                                #########################################################################################################################################################
                                
                                
                                if i==1:

                                    lenf5=len(sda2)

                                    sda3=sda2
                                 
                                    lenf5=len(sda3)
                                    
                                    
                                    #Extract
                            
                                    s=""

                                    sda3=sda2
                                    lenf6=len(sda3)
                                    
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                  
                                    sda17=""
                   
                                    g=0

                                    sda3=sda2

                                    lenf6=len(sda3)                      
                                    sda17=""
                                
                                    sda3=sda2
                                    
                                    lenf6=len(sda3)
                                
                                    szx=""

                                    sda6=""

                                    #Compression

                                    sda10=""
                                    sda11=""
                                    
                                    sda17=""

                                    

                                    ei=0
                                    former=0

                                    while ei<lenf6:
                                            sda4=sda3[ei:ei+1]
                                            if sda4=="1":
                                                    sda11=bin(former)[2:]
                                                    T10=len(sda11)
                                                    if Circle_times2>0:
                                                            if former==0:
                                                                sda11=="0000"
                                                            if former==1:
                                                                sda11=="0001"
                                                            if former==2:
                                                                sda11=="0010"
                                                            if former==3:
                                                                sda11=="0011"
                                                            if former==4:
                                                                sda11=="0100"
                                                            if former==5:
                                                                sda11=="0101"
                                                            if former==6:
                                                                sda11=="0110"
                                                            if former==7:
                                                                sda11=="0111"
                                                            if former==8:
                                                                sda11=="1000"
                                                            if former==9:
                                                                sda11=="1001"
                                                            if former==10:
                                                                sda11=="1010"
                                                            if former==11:
                                                                sda11=="1011"
                                                            if former==12:
                                                                sda11=="1100"
                                                            if former==13: 
                                                                sda11=="1101"   
                                                            if former==14: 
                                                                sda11=="1110" 
                                                            if former==15: 
                                                                sda11=="1111"   
                                                            if former>15:
                                                                raise SystemExit
                                                    if Circle_times2==0:
                                                            if former==0:
                                                                sda11="00000"
                                                            if former==1:
                                                                sda11="00001"
                                                            if former==2:
                                                                sda11="00010"
                                                            if former==3:
                                                                sda11="00011"
                                                            if former==4:
                                                                sda11="00100"
                                                            if former==5:
                                                                sda11="00101"
                                                            if former==6:
                                                                sda11="00110"
                                                            if former==7:
                                                                sda11="00111"
                                                            if former==8:
                                                                sda11="01000"
                                                            if former==9:
                                                                sda11="01001"
                                                            if former==10:
                                                                sda11="01010"
                                                            if former==11:
                                                                sda11="01011"
                                                            if former==12:
                                                                sda11="01100"
                                                            if former==13: 
                                                                sda11="01101"   
                                                            if former==14: 
                                                                 sda11="01110" 
                                                            if former==15: 
                                                                  sda11="01111"   
                                                            if former==16: 
                                                                  sda11="10000" 
                                                            if former==17: 
                                                                  sda11="10001"   
                                                            if former==19: 
                                                                  sda11="10010" 
                                                            if former==20: 
                                                                  sda11="10011"  
                                                            if former==21: 
                                                                  sda11="10100" 
                                                            if former==22: 
                                                                  sda11="10101" 
                                                            if former==23: 
                                                                  sda11="10110"
                                                            if former==24: 
                                                                  sda11="11000"  
                                                            if former==25: 
                                                                  sda11="11001"
                                                            if former==26: 
                                                                  sda11="11010"
                                                            if former==27: 
                                                                  sda11="11011"    
                                                            if former==28: 
                                                                  sda11="11100"
                                                            if former==29: 
                                                                  sda11="11101"
                                                            if former==30: 
                                                                  sda11="11110" 
                                                            if former==31: 
                                                                  sda11="11111"
                                                            if former>31:
                                                                raise SystemExit
                                                    sda10=sda10+sda11
                                                    former=0
                                                                                                   
                                            former=former+1
                                            ei=ei+1
                                                      
                                            
                 
                                    sda17=sda10
                                    
                                    #print(sda17)
                              
                                    
                                    lenfS=len(sda17)
                                    #print(lenfS)

                                   
                                    Circle_times2=Circle_times2+1
                          
                                    sda2=sda17


                                    if  lenfS<=160:
                                             sda171=bin(Circle_times2)[2:]
                                             lenf=len(sda171)
                                        
                                             szx1=""
                                             xc=48-lenf%48
                                             z=0
                                             if xc!=48:
                                                     while z<xc:
                                                         szx1="0"+szx1
                                                         z=z+1
   
                               

                                    if  lenfS<=160:

                                                
                                             sda17="1"+sda17
                                             lenf=len(sda17)
                                        
                                             szx=""
                                             xc=8-lenf%8
                                             z=0
                                             if xc!=8:
                                                     while z<xc:
                                                         szx="0"+szx
                                                         z=z+1
   
                                    
                                             lenf=len(sda17)
                                            
                                             sda17=szx1+sda171+szx+sda17
                                             #print(len(sda17))

                                    if   lenfS<=160:
                                                
                                    		L=len(sda17)
                                    		n = int(sda17, 2)
                                    		qqwslenf=len(sda17)
                                    		qqwslenf=(qqwslenf//8)*2
                                    		qqwslenf=str(qqwslenf)
                                    		qqwslenf="%0"+qqwslenf+"x"
                                    		jl=binascii.unhexlify(qqwslenf % n)
                                    		sssssw=len(jl)
                                    		szxzzza=""
                                    		szxzs=""
                                    		sda2=sda6
                                    		
                                    		with open(nameas, "wb") as f2:
                                    			f2.write(jl)
                                    	
                                    		x2 = time()
                                    		x3=x2-x
                                    		xs=float(x3)
                                    		return print(x3)
                                    		
                                if i==2:

                                    sda17=""
                              
                                    sda3=sda2
                                    
                                    lenf6=len(sda3)

                                    szx=""

                                    sda6=""

                                    #Extract

                                    sda10=""
                                    sda11=""
                                  
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                
                                    T7=0
                                    T9=0
                                 
                                    if C==1:
                                        if   Circle_times2==0:

                                                sda11=sda3[0:8]
                                                xc3 = int(sda11, 2)
                                                if xc3>7:
                                                        Corrupted=1
                                                sda3=sda3[8:]
                                                lenf6=len(sda3)

                                                sda10=sda3[0:16]
                                                Deep5 = int(sda10, 2)
                                                Deep5=Deep5+2
                                                Deep4=Deep5-1
                                                sda3=sda3[16:]
                                                lenf6=len(sda3)
                                                Deep7=Deep5-2
                                                
                                                sda6=sda3[0:48]
                                                T = int(sda6, 2)
                                                sda3=sda3[48:]
                                                lenf6=len(sda3)
                                                print("Deep: ")
                                                print(Deep7)
                                                
                                        if   Circle_times2>0:
                                        	xc3=0
                                        
                                        if C==1 and T!=0:
                                                sda3=sda3[xc3:]
                                                lenf6=len(sda3)
                                                sda4=sda3[lenf6-Deep4:lenf6-1]
                                                sda6=sda3[lenf6-(Deep4-1):lenf6-1]
                                                sda5=sda3[lenf6-1:lenf6]
                                                sda3=sda3[0:lenf6-Deep4]
                                        
                                                T7 = int(sda3, 2)
                                                T11 = int(sda4, 2)
                                                T12 = int(sda6, 2)
                                                T9 = int(sda5, 2)

                                                if sda5=="0":
                                                        e=((2**Deep5)-1)+(2**Deep5-7)-1
                                                        T8=T11
                                                if sda5=="1":
                                                        e=((2**(Deep2+1))-1)+(2**(Deep2-6))-1
                                                        T8=T12
                                                j=e+T8
                                                T7=T7+1
                                                T7=T7*j
                                                
                                       
                                    sda6=sda4
                                    sda4=""
                                      
                                    #####################################################################################################################################################
                                   
                                    sda5=""
                                    
                                    
                                    sda17=bin(T7)[2:]
                                     
                                    sda2=sda17
                                   

                                    if i==2:
                                        wer=""
                                        wer=sda6
                                        sda4=""
                                        szx=""
                                        if C==1 and T!=0:
                                                Circle_times2=Circle_times2+1

                                        lenf9=len(sda17)
                                        #print(Circle_times2)
                                        
                                        
                                        if  Circle_times2==T:
                                        	   
                                            if C==1 and T==0:
                                            	sda17=sda3
                                            	lenf=len(sda17)
                                            	szx=""
                                            	xc=8-lenf%8
                                            	z=0
                                            	if xc!=0:
                                            	        if xc!=8:
                                            	            while z<xc:
                                            	            	szx="0"+szx
                                            	            	z=z+1
                                            	sda17=szx+sda17
                                        
                                            if C==1 and T!=0:
 
                                            	sda17=bin(T7)[3:]
                                            	lenf14=len(sda17)
                                            	#print(lenf14)
                                            	lenf16=lenf14%8
                                            	if lenf16!=0 or lenf14>=((2**40)-1)*8 or Corrupted==1:

                                            		print("file corrupted")
                                            		raise SystemExit
                                            		
                                            	
                                            	lenf=len(sda17)
                                            	szx=""
                                            	xc=8-lenf%8
                                            	z=0
                                            	if xc!=0:
                                            	        if xc!=8:
                                            	            while z<xc:
                                            	            	szx="0"+szx
                                            	            	z=z+1
                                            	sda17=szx+sda17

                                            L=len(sda17)
                                         
                                            n = int(sda17, 2)
                                            qqwslenf=len(sda17)
                                            qqwslenf=(qqwslenf//8)*2
                                            qqwslenf=str(qqwslenf)
                                            qqwslenf="%0"+qqwslenf+"x"
                                            jl=binascii.unhexlify(qqwslenf % n)
                                            sssssw=len(jl)

                                            szxzzza=""
                                            szxzs=""
                                            sda2=sda6
                                             
                                            with open(nameas, "wb") as f2:
                                            
                                              
                                            	f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)
   
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
