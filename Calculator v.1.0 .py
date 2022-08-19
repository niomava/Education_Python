print("$" * 10, "Калькулятор v 1.0", "$" * 10)

while True:
    print("Введите q для выхода")
    s = input("Знак (+,-,*,/): ")
    
    if s == 'q': break

    if s not in ('+', '-', '*', '/'):
            print("неверный знак")
            continue
            
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))

    if s == "+":
        print("%.2f" % (x + y))
    elif s == "-":
        print("%.2f" % (x - y))
    elif s == "*":
        print("%.2f" % (x * y))
    elif s == "/":
        
        if y != 0:
            print("%.2f" % (x / y))
        else:
            print("Деление на ноль")
