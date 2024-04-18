def factorial(n):
    if n!=1:
        fac=n*factorial(n-1)
        return(fac)
    else:
        return(n)

n=int(input("Please enter a number: "))
if n<0:
    facto="No factorial exists for negative numbers."
elif n==0:
    facto=1
else:
    facto=factorial(n)
print(facto)
