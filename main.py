from Dino import Dino
from DinoParque import DinoParque
from datetime import datetime
from datos import getDatos
from func import imprimirListado, opciones

dinos = getDatos(0)
dinoParque1 = DinoParque(1, "Rocoso", dinos)
while True:
    imprimirListado(dinoParque1)
    print()
    opciones()

    opcion = input("Selecciona opción: ")
    
    if opcion == "O":
        print("Ordenar por:")
        print("1 - Nombre")
        print("2 - Altura")
        print("3 - Peso")
        subopcion = input("Elige una opción: ")

        if subopcion == "1":
            dinoParque1.DinosHabitantes.sort(key=lambda d: d.nombre)
        elif subopcion == "2":
            dinoParque1.DinosHabitantes.sort(key=lambda d: d.altura)
        elif subopcion == "3":
            dinoParque1.DinosHabitantes.sort(key=lambda d: d.peso)
        else:
            print("Opción inválida")
        
        print("\nListado ordenado:")
    if opcion == "A":
        dinoId = int(input("¿ID?: "))
        nombre = input("Nombre:")
        habilidades = input("Habilidades separadas por comas:  ")
        habilidadesLista = habilidades.split(",")
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))
        carnivoro = input("Es carnivoro [S/N]")
        if carnivoro == "S":
            carnivoro == True
        else:
            False
        omnivoro = input("Es omnivoro [S/N]")
        if omnivoro == "S":
            omnivoro == True
        else:
            False
        herbivoro = input("Es herbivoro [S/N]")
        if herbivoro == "S":
            herbivoro == True
        else:
            False
        descubrimiento = input("Fecha de descubrimiento (dd-mm-yyyy): ")
        descubrimientoFecha = datetime.strptime(descubrimiento, "%d-%m-%Y")
        esqueletoCompleto = input("Fecha en la que se completo el esqueleto (dd-mm-yyyy): ")
        esqueletoCompletoFecha = datetime.strptime(esqueletoCompleto, "%d-%m-%Y")
        
        dinoAñadido = Dino(dinoId, nombre, habilidadesLista, altura, peso, carnivoro, omnivoro, herbivoro, descubrimientoFecha, esqueletoCompletoFecha )
        dinoParque1.añadirDino(dinoAñadido)

    if opcion == "S":
        break
