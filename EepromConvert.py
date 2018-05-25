data=[]

filename=raw_input ('Enter file name:')
fobj=open(filename,'r')
data_raw=fobj.read()
for i in range(0,len(data_raw),3):
        if data_raw[i]!=' ':
            data.append('0x'+data_raw[i]+data_raw[i+1]+',')
            if i%25==0 and i!=0:
                    data.append('\r')
        else:
            data.append(' ')

foutput=open('EEPROMHex.txt','w')
foutput.writelines(data)     
fobj.close()
foutput.close()
print "OK"

