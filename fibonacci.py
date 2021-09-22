import time

prevNumber = 0
currentNumber = 1

def fibonacci(number1, number2):
    global prevNumber
    global currentNumber
    total = number1 + number2
    prevNumber = number2
    currentNumber = total
    print(total)
    time.sleep(1)
    if currentNumber > 100000000:
        return ""
    fibonacci(prevNumber, currentNumber)