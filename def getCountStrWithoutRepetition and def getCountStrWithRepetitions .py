import itertools

def getCountStrWithoutRepetitions(charList):
    x = charList.split()
    No_Repeat_charlist=list(itertools.permutations(x))
    Сount_option_nrp=len(No_Repeat_charlist)
    print("Количество комбинаций строк без повторений: ", Сount_option_nrp)
getCountStrWithoutRepetitions("q w e r t y")

def getCountStrWithRepetitions(charList):
    x = charList.split()
    Repeat_charlist = list(itertools.product(x, repeat=len(x)))
    Сount_option_rp = len(Repeat_charlist)
    print("Количество комбинаций строк с повторениями: ", Сount_option_rp)
getCountStrWithRepetitions("q w e r t y")