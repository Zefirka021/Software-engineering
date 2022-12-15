n = int(input("Введите число: "))

def f(n):
    def f1(n):
        return (n)
    return(f1(n) + n)
print(f(n))
