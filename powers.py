n=int(input("Please enter a number: "))
i=0
S_C=0
while i<=n and S_C==0:
    if i*i==n:
        S_C=1
    elif i*i*i==n:
        S_C=2
    if i*i==n and i*i*i==n:
        S_C=3
    i=i+1
if S_C==1:
    print(n,"is a perfect square.")
elif S_C==2:
    print(n,"is a perfect cube.")
elif S_C==3:
    print(n,"is a perfect square and a perfect cube.")
else:
    print(n,"is a not perfect square or a perfect cube.")
