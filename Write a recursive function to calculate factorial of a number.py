def fect(n):
    if n==1:
        return 1
    else:
        return(n*fect(n-1))

n=int(input("enter the number to print fectorial of a number"))
print(fect(n))