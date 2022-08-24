import math

def getCountStrWithoutRepetitions(charList):
    N = len(list(charList))
    NN = math.factorial(N)
    K = 6
    R = math.factorial(N-K)
    print("Количество комбинаций строк без повторений: ",NN/(R))
getCountStrWithoutRepetitions(["a","b","c","d","e","f"])

def getCountStrWithRepetitions(charList):
    N = len(list(charList))
    K = 6
    print("Количество комбинаций строк с повторениями: ",N**K)
getCountStrWithRepetitions(["a","b","c","d","e","f"])