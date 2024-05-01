
# the dimensions of the array
height = 3
width = 4

# the list
list2d = [ [0] * width for r in range(height) ]

# fill the 2-dim array
for i in range(height):
    for j in range(width):
        list2d[i][j] = " " + str(i) + str(j)

# print the 2-dim array
for i in range(height):
    line = ""
    for j in range(width):
        line += list2d[i][j];

    print(line)

# the checkpoint activity
columnNum = int(input("Enter the column number: "))
if columnNum <= width:
    for i in range(height):
        print(list2d[i][columnNum - 1])
else:
    print("Column Does Not Exist")
