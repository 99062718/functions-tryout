import time

prevNumber = 0
currentNumber = 1

while currentNumber < 10000000:
    print(fibonacci(prevNumber, currentNumber))
    time.sleep(1)

def fibonacci(number1, number2):
    global prevNumber
    global currentNumber
    total = number1 + number2
    prevNumber = number2
    currentNumber = total
    return total
