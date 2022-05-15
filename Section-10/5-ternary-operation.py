

number_value = int(input("Introduce un número: "))


msg = "Impar" if number_value % 2 != 0 else "Par"


print("El número introducido que es {1} es {0}".format(msg, number_value))