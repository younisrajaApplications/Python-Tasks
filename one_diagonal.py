##
size = int(input("Size of the square: "))
ln = 0
while ln < size:
    line = ""
    position = 0
    while position < size:
        if position == ln:
            line += "x"
        else:
            line += "o"
        position = position + 1
    print (line)
    ln = ln + 1
##
