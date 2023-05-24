num = int(input("Ingresa un número entero: "))

if num % 2 == 0 and num % 3 == 0:
    print(f"{num} es múltiplo de 2 y de 3 a la vez.")
else:
    print(f"{num} no es múltiplo de 2 y de 3 a la vez.")
