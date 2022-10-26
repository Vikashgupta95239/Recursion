def Revan(n):
    if(n%2==0):
        print(n)
    if n==1:
        return 1
    else:
        Revan(n-1)
        
n=int(input("enter the number to print evan number in reverse order"))
Revan(n) 

        
    
    

