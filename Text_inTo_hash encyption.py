A=list(input('Enter A password =>'))
D=0
for T in A :
    MF=hex(ord(T)+D)
    A[D]=MF[3:]
    D=D+1  
AA=''.join(A)  
print(AA)