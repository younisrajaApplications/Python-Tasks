##
size = int(input("Size of the square: "))
ln = 0
while ln < size:
    line = ""
    position = 0
    while position < size:
        if ln + position == size - 1:
            line += "x"
        elif position == ln:
            line += "x"
        else:
            line += "o"
        position += 1
    print (line)
    ln += 1
##
