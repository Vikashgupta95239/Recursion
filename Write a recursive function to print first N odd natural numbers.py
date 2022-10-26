def odd(n):
    if n==0:
        return 1
    else:
        odd(n-1)
        if(n%2!=0):
            print(n)
n=int(input("enter the number"))              
odd(n)
