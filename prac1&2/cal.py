num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))


operation = input("Enter any one operation (+,-,*,/,^,%) ")


print("addition of two number is : ", num1 + num2)
print("sub of two number is : ", num1 - num2)
print("division of two operation is : ", num1 / num2)
print("multi of two operation is : ", num1 * num2)
print("exp of two operation is : ", num1 ** num2)
print("modulo of two operation is : ", num1 % num2)



if operation == "+" :
    print("addition of two number is : ", num1 + num2)
elif operation == "-" :
    print("sub of two number is : ", num1 - num2)
elif operation == "/" :
    print("division of two operation is : ", num1 / num2)
elif operation == "*" :
    print("multi of two operation is : ", num1 * num2)
elif operation == "**" :
    print("exp of two operation is : ", num1 ** num2)
elif operation == "%" :
    print("modulo of two operation is : ", num1 % num2)

