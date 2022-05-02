# Variables globales sin usar uso de palabra "global"
"""
PRIMER CASO CON SOLO VARIABLE GLOBAL
variable_global = "Hola Mundo"
def custom_function():
    print(variable_global)

print("Fuera: " + variable_global)
# LLamar a la función para ejecutarla
custom_function()"""


variable_global = "Hola Mundo"
def custom_function():
    variable_global = "Hola Alexis"
    print("Dentro de: "+ variable_global)

print("Fuera: " + variable_global)
# LLamar a la función para ejecutarla
custom_function()