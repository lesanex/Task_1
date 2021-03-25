st = input("Введите текст\n")
gl = ["a", "o", "u", "i", "e", "y"]


for i in gl:
    print(i, st.count(i), end=", " if gl[-1] != i else "")

