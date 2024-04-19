def population_size(n):
    if n == 0:
        return(100)
    else:
        return(3/2 * population_size(n - 1) + population_size(n - 1))

def better_population_size(n):
    if n == 0:
        return(100)
    else:
        return(0.1 * (1 - better_population_size(n - 1)/10000) * better_population_size(n - 1) + better_population_size(n - 1))

n = int(input("Enter the year: "))
#population = population_size(n)
#print(population)
#population = better_population_size(n)
#print(population)

"""Difference in size after 50 years: better_popolation_size() gives a significantly smaller result."""
m = 100
for i in range(0,n):
    m = 3/2*m + m
print(m)
m = 100
for i in range(0,n):
    m = 0.1*(1 - m/10000)*m + m
print(m)
