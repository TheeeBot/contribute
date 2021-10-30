N=int(input())
for i in range(N):
    X=int(input())
    soma=0
    if X>0:
        for j in range(1,X):
            if X % j == 0:
                soma=soma+j
    if soma==X and X!=0:
        print ("%d eh perfeito" % X)
    else:
        print ("%d nao eh perfeito" % X)
