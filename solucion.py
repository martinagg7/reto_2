from math import ceil
t=int(input())
for _ in range(t):
    a,b,c=input().split()#a=numero de filas, b=numero de columnas, c=numero de dias
    a=int(a)
    b=int(b)
    c=int(c)
    d=abs(a-b)
    print(ceil(d//2*c))



