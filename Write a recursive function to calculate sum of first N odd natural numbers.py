def oddsum(n):
    if n==1:
        return 1
    else:
        return(2*n-1+oddsum(n-1))
    
    
    
n=int(input("enter the number to print sum of odd number"))
print(oddsum(n))