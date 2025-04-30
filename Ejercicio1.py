#Ejercicio #1
#version datos dinamicos
# Ejercicio #1
def sumar_numeros():
    try:
        N = int(input("Ingrese la cantidad de números (N): "))
        if N <= 0:
            raise ValueError("El número debe ser mayor que 0.")
        SUM = 0
        for i in range(N):
            while True:
                try:
                    x = float(input(f"Ingrese x_{i+1}: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            SUM += x
        print("La suma es:", SUM)
    except ValueError as e:
        print(f"Error: {e}")

def main():
    try:
        sumar_numeros()
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

if __name__ == "__main__":
    main()