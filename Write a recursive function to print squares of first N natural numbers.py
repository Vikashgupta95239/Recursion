def square(n):
    if n==0:
        return 1
    else:
       square(n-1)
    print(n*n)
n=int(input("enter the number"))
square(n)

