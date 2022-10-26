def Rnatural(n):
    if n==1:
        return 1
    k=n+Rnatural(n-1)
    return k   
n=int(input("enter the number"))
l=Rnatural(n)
print(l)

