def febonacci(n):
    if n==0:
        return 0
    a=1
    b=-1
    sum=a+b
    print(sum)
    b=a
    a=sum
    else:
        
        return (febonacci(n-1))
        
n=int(input("enter the number to print febonacci series"))
febonacci(n)
    