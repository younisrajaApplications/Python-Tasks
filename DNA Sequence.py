def sequence_count(sequence):
    a=0
    c=0
    g=0
    t=0
    for i in range(0, len(sequence)):
        if sequence[i] == "A":
            a += 1
        elif sequence[i] == "C":
            c += 1
        elif sequence[i] == "G":
            g += 1
        elif sequence[i] == "T":
            t += 1
    return ("A:"+ str(a) + " C:" + str(c)+ " G:" + str(g) + " T:" + str(t))

print(sequence_count("AAAAAAGGGCCCCTTAGTC"))
print(sequence_count("AACCGTA"))
