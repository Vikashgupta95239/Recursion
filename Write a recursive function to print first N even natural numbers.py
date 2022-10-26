def evan(n):
    if n==1:
        return 1
    evan(n-1)
    if(n%2==0):
        print(n)
n=int(input("enter the number "))
evan(n)
