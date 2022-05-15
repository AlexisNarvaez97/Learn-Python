# Operadores lógicos OR

a = 1 == 1 or 1 > 0 # True
a = 1 != 1 or 1 > 0 or 45 <= 90  # True
a = 1 != 2 or 1 > 0 or 45 > 90  # False
a = 1 != 2 or 1 > 0 or 45 <= 90 or 45 != 78  # True
a = 1 != 2 or 0 >= 0 # True
a = 1 <= 2 or 1 > 0 #True

print("Final")