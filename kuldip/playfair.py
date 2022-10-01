import numpy as np

msg = input('Enter massage:')
key = input("Enter KeyWord:")
Type = int(input("Prees [1] For Encryption And Press [2] for Decryption : "))

key=key.replace(' ','')
key=key.lower()
msg1=msg.replace(' ','')
msg1=msg1.lower()

for i in range(0,len(msg1),2):
    if(i+1<len(msg1)):
        if(msg1[i]==msg1[i+1]):
            msg1=msg1[0:i+1]+'x'+msg1[i+1:len(msg1)]

if(len(msg1)%2==1):
    msg1=msg1+'x'
ct=''
alph="abcdefghijklmnopqrstuvwxyz"
f_key=key+alph
met=np.array([[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]])
count=0
ss=0
for i in range(0,5):
    for j in range(0,5):
        while(ss == 0 ):
                a=ord(f_key[count])-97
                if(a==8 or a==9):
                    a=8
                if(a not in met):
                    ss=1
                    met[i,j]=a
                    count=count+1
                else:
                    count=count+1
        ss=0
if(Type==1):
   
    for i in range(0,len(msg1),2):
        a1=ord(msg1[i])-97
        a2=ord(msg1[i+1])-97
        ind1=np.where(met == a1)
        ind2=np.where(met == a2)
        if(ind1[0][0]==ind2[0][0]):
            ct=ct+chr(met[ind1[0][0],(ind1[1][0]+1)%5]+97)
            ct=ct+chr(met[ind2[0][0],(ind2[1][0]+1)%5]+97)
        elif(ind1[1][0]==ind2[1][0]):
            ct=ct+chr(met[(ind1[0][0]+1)%5,ind1[1][0]]+97)
            ct=ct+chr(met[(ind2[0][0]+1)%5,ind2[1][0]]+97)
        else:
            ct=ct+chr(met[ind1[0][0],ind2[1][0]]+97)
            ct=ct+chr(met[ind2[0][0],ind1[1][0]]+97)
    print(ct)
    
else:
    for i in range(0,len(msg1),2):
        a1=ord(msg1[i])-97
        a2=ord(msg1[i+1])-97
        ind1=np.where(met == a1)
        ind2=np.where(met == a2)
        if(ind1[0][0]==ind2[0][0]):
            ct=ct+chr(met[ind1[0][0],(ind1[1][0]-1)%5]+97)
            ct=ct+chr(met[ind2[0][0],(ind2[1][0]-1)%5]+97)
        elif(ind1[1][0]==ind2[1][0]):
            ct=ct+chr(met[(ind1[0][0]-1)%5,ind1[1][0]]+97)
            ct=ct+chr(met[(ind2[0][0]-1)%5,ind2[1][0]]+97)
        else:
            ct=ct+chr(met[ind1[0][0],ind2[1][0]]+97)
            ct=ct+chr(met[ind2[0][0],ind1[1][0]]+97)
    print(ct)