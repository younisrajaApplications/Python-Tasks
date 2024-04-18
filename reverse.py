number=int(input("Please enter a number: "))
num=number
if number<0:
    num=number*-1
match=0
num=str(num)
for i in range(0,len(num)):
    if num[i]==num[len(num)-1-i]:
        match=match+1
if match==len(num):
    print("The number",number,"is a palindrome.")
else:
    print("The number",number,"is a not palindrome.")
