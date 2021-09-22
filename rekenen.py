def addition(number1:int, number2:int) -> str:
    return str(number1) + " + " + str(number2) + " = " + str(number1 + number2)

def subtraction(number1:int, number2:int) -> str:
    return str(number1) + " - " + str(number2) + " = " + str(number1 - number2)

def multiplication(number1:int, number2:int) -> str:
    return str(number1) + " * " + str(number2) + " = " + str(number1 * number2)

def division(number1:int, number2:int) -> str:
    return str(number1) + " / " + str(number2) + " = " + str(number1 / number2)

def increment(number1:int) -> str:
    return str(number1) + " + 1 = " + str(number1 + 1)

def decrement(number1:int) -> str:
    return str(number1) + " - 1 = " + str(number1 - 1)

print(addition(12, 17))
print(addition(30, 19))
print(addition(0, 55))

print(subtraction(2, 1))
print(subtraction(57, 10))
print(subtraction(202, 164))

print(multiplication(5, 2))
print(multiplication(14, 5))
print(multiplication(55, 202))

print(division(1, 2))
print(division(100, 5))
print(division(50, 3))

print(increment(55))
print(increment(1034))
print(increment(333))

print(decrement(42))
print(decrement(5022))
print(decrement(30))