def Esum(n):
    if n==2:
        return 2
    else:
        return(2*n+Esum(n-1))

n=int(input("enter the number to print sum of evan number"))  
print(Esum(n))  