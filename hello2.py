antwoord = int(input("Hoe vaak moet hello world geprint worden? "))

def helloWorld(nummer:int):
    for x in range(1, nummer+1):
        print(str(x), ". Hello World!")

helloWorld(antwoord)