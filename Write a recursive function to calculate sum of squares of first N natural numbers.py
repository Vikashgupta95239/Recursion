def Sqsum(n):
    if n==1:
        return 1
    else:
        return n*n+Sqsum(n-1)
n=int(input("ente the number to print square of n number"))

print(Sqsum(n))

