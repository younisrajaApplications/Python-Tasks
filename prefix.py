first_String=input("Please enter the prefix: ").title()
second_String=input("Please enter the word: ").title()
match=0
print(first_String,second_String)
for i in range(0,len(first_String)):
    if first_String[i]==second_String[i]:
        match=match+1
if match==len(first_String):
    print("The first string entered is a prefix of the second string.")
else:
    print("The first string entered is not a prefix of the second word.")
