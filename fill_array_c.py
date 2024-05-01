arrayLength = int(input("Enter the length of the array: "))

numbers = [0] * arrayLength

for i in range(arrayLength):
  numbers[i] = 1

for i in range(arrayLength):
    if i % 2 == 0:
        print("numbers[" + str(i) + "] = " + str(0))
    else:
        print("numbers[" + str(i) + "] = " + str(1))
