t=0
sumpoz=0
sumneg=0
c=0
nrpoz=0
nrneg=0

while c<12:
    
    t=eval(input('Introduceti temperatura:'))
    
    if t>0 : 
        sumpoz=sumpoz+t
        nrpoz+=1

    else :
        sumneg = sumneg + t
        nrneg+=1
    
    c=c+1
if nrpoz != 0:
    print('media pozitiva =', sumpoz/nrpoz)
else : print ('nu exista valori pozitive')

if nrneg != 0:
    print('media negativa =' , sumneg/nrneg)
else : print ('nu exista valori negative')