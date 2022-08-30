import math


def getCountStrWithoutRepetitions(charList):
    N = len(list(charList))
    NN = math.factorial(N)
    result = 0
    for K in range(1,N+1):
        R1 = math.factorial(N - K)
        result += (NN / R1)
    print("Количество комбинаций для всех длин строк без повторений: ", result)

getCountStrWithoutRepetitions(["a","b", "c"])


def getCountStrWithRepetitions(charList):
    N = len(list(charList))
    result = 0
    for K in range(1,N+1):
        result += N ** K
    print("Количество комбинаций для всех длин строк с повторениями: ", result)

getCountStrWithRepetitions(["a", "b", "c"])
