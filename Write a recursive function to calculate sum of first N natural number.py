def Nsum(n):
    if n==0:
        return 1
    else:
        return n+Nsum(n-1)


n=int(input("enter the number"))
print(Nsum(n))