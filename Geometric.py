def geo(r , n):
    if n == 1:
        return (1)
    else:
        nth = r * geo(r , n-1)
        return(nth)
    
r = float(input())
n = int(input())

nth = geo(r , n)
print(nth)
