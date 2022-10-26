def Sqsum(n):
    if n==1:
        return 1
    else:
        return n*n*n+Sqsum(n-1)


n=int(input("ente the number to print cube of n number"))

print(Sqsum(n))
