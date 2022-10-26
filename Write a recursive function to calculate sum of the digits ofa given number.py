def Sumdigit(n):
    if n/10==0:
        return n
    else:
        return (n%10+Sumdigit(n//10))
n=int(input("enter the number to calculate the sum of digit"))
print(int(Sumdigit(n)))
