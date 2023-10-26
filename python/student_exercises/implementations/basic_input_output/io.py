number1 = int(input("Enter number 1 "))
number2 = input("Enter number 2 ")

result = number1*float(number2)

firstname = "Antonio"
lastname = "Pisanello"
fullname1 = firstname + " " + lastname
fullname2 = f"{firstname} {lastname}"

print(fullname1)
print(fullname2)


print("Number1: " + str(number1) + " * Number2 " + str(number2) + " = " + str(result))
print(f"Number1: {number1} * Number2 {(number2)} = {result}")
print("Number1: {} * Number2 {} = {}".format(number1, number2, result))
print("Number1: %d * Number2 %s = %f"%(number1, (number2), result))

