#lista de nombre
nombres = ["Ana", "Carlos", "María", "Juan", "Sofía"]

#Diccionario de edades
edades = {
  "Ana": 30,
  "Carlos": 25,
  "María": 28,
  "Juan": 35,
  "Sofía": 22,
}

#Solicitar al usuario  que ingrese un nombre y luego mostrar la edad de esa persona si esta en el diccionario

nombre_buscar = input("Ingresa un nombre: ")

if nombre_buscar in edades:
    print(f"{nombre_buscar} tiene {edades[nombre_buscar]} años.")

else:
    print(f"La persona '{nombre_buscar}' no fue encontrada.")
