# Lista de nombres
nombres = ["Ana", "Carlos", "María", "Juan", "Sofía"]

# Diccionario de edades
edades = {
    "Ana": 30,
    "Carlos": 25,
    "María": 28,
    "Juan": 35,
    "Sofía": 22,
}

while True:

    print("""
¿Qué desea hacer?
1. Buscar una persona
2. Ver personas registradas
3. Salir
""")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Solicitar al usuario que ingrese un nombre
        nombre_buscado = input("Ingresa un nombre: ")

        nombre_buscado = nombre_buscado.strip().capitalize()

        # Verificar si el nombre existe en el diccionario
        if nombre_buscado in edades:

            print(f"{nombre_buscado} tiene {edades[nombre_buscado]} años.")

        else:

            print(f"La persona '{nombre_buscado}' no fue encontrada.")

            agregar = input("¿Desea agregar esta persona? (S/N): ")

            if agregar.strip().upper() == "S":

                edad = int(input("Ingrese la edad: "))

                nombres.append(nombre_buscado)
                edades[nombre_buscado] = edad

                print("Persona agregada correctamente.")

    elif opcion == "2":

        print(f"\nHay {len(nombres)} personas registradas.")
        print("Personas registradas:")

        for nombre in nombres:
            print(f"- {nombre}")

    elif opcion == "3":

        break

    else:

        print("Opción no válida.")