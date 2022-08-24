import math


def getCountStrWithoutRepetitions(charList):
    N = len(list(charList))
    NN = math.factorial(N)
    K = int(input("Введите конечную длину строки: "))
    if K <= N and K != 0:
        R = math.factorial(N - K)
        print("Количество комбинаций строк без повторений: ", NN / (R))
    if K > N or K == 0:
        print("Недопустимая длина строки: ")


getCountStrWithoutRepetitions(["a", "b", "c", "d", "e", "f"])


def getCountStrWithRepetitions(charList):
    N = len(list(charList))
    K = int(input("Введите конечную длину строки: "))
    if K <= N and K != 0:
        print("Количество комбинаций строк с повторениями: ", N ** K)
    if K > N or K == 0:
        print("Недопустимая длина строки: ")


getCountStrWithRepetitions(["a", "b", "c", "d", "e", "f"])
