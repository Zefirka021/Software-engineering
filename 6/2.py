n = int(input("Введите число: "))

f1 = lambda n: n + n
f2 = lambda n: n * n
print(f1(f2(n)))
