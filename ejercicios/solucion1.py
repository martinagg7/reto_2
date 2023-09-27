from math import ceil
n=int(input("Ingrese un numero: "))
for _ in range(n):
    a,b,c=map(int,input().split())
    print(ceil(a-b/2*c))




