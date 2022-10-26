def Rodd(n):
    if n%2!=0:
        print(n)
    if(n==1):
        return 1
    else:
        Rodd(n-1)
# n=int(input("enter the number"))
Rodd(90)

