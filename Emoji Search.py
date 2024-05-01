file = open("emoji-formatted.txt","r")
search = input("Enter keyword: ")
for line in file:
    if search in line:
        emoji = line.split(" ")
        print(emoji[0])
print("You happy now?")
