n=eval(input('Introduceti un numar:'))
med=0
suma=0
prod=1
i=1
while i<=n:
    suma=suma+i
    prod*=i
    med=suma/n
    i=i+1
# print(n)
print('suma numerelor de la 1 la ', n , ' este egala cu :', suma)
print('produsul numerelor de la 1 la ', n , 'este egala cu :',prod)
print('media numerelor de la 1 la ', n , 'este egala cu :', med)
