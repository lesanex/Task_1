num = int(input("Введите число: \n"))
sings = input().split()

while sings[0] != "=":
    if sings[0] == "+":
        num += float(sings[1])
        sings = input().split()
    elif sings[0] == "-":
        num -= float(sings[1])
        sings = input().split()
    elif sings[0] == "*":
        num *= float(sings[1])
        sings = input().split()
    elif sings[0] == "/":
        num /= float(sings[1])
        sings = input().split()
    elif sings[0] == "**":
        num **= float(sings[1])
        sings = input().split()
    else:
        print("Введеного знака не существует")
        break
print("Ответ:", num)