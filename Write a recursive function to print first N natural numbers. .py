
def Natural(n):
    if n==0:
        return 1
    Natural(n-1)
    print(n)
n=int(input("enter the number"))
Natural(n)


