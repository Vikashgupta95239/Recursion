def square(n):
    print(n*n*n)
    if n==1:
        return 1
    else:
       square(n-1)
    
n=int(input("enter the number"))
square(n)