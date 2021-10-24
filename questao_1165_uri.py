# -*- coding: utf-8 -*-
n=int(input())
for i in range(n):
    numero=int(input())
    tentativa=0
    if numero%1==0:
        tentativa+=1
    for i in range(2,numero):
        if numero % i == 0:
            print ("%d nao eh primo" %numero)
            break
    else:
        print ("%d eh primo"%numero)
