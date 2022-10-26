def Rsquare(n):
    print(n*n)
    if n==1:
        return 1
    else:
        Rsquare(n-1)
n=int(input("enter the number"))
Rsquare(n)