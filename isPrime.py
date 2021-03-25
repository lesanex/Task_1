print("Введите число: ")
num = input()
s = 0
if num == "0":
    print("Введите число больше 0")
elif not num.isdigit():
    print("Ошибка ввода, введите число")
else:
    num_integer = int(num)
    for i in range (2, num_integer // 2 + 1):
        if (num_integer % i == 0):
            s += 1
    if (s > 0):
        print("Число", num_integer, "простым не является")
    else:
        print(num_integer, "простое число")

