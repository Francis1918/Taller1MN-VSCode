def iterative_fibonacci(n):
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        for i in range(1, n):
            z = x + y
            x = y
            y = z
        return y

# Ejemplo de uso
n = 11
y = iterative_fibonacci(n)
print(f"El término {n} de la sucesión de Fibonacci es: {y}")