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
            carnivoro = True
        else:
            False
        omnivoro = input("Es omnivoro [S/N]")
        if omnivoro == "S":
            omnivoro = True
        else:
            False
        herbivoro = input("Es herbivoro [S/N]")
        if herbivoro == "S":
            herbivoro = True
        else:
            False
        descubrimiento = input("Fecha de descubrimiento (dd-mm-yyyy): ")
        descubrimientoFecha = datetime.strptime(descubrimiento, "%d-%m-%Y")
        esqueletoCompleto = input("Fecha en la que se completo el esqueleto (dd-mm-yyyy): ")
        esqueletoCompletoFecha = datetime.strptime(esqueletoCompleto, "%d-%m-%Y")
        
        dinoAñadido = Dino(dinoId, nombre, habilidadesLista, altura, peso, carnivoro, omnivoro, herbivoro, descubrimientoFecha, esqueletoCompletoFecha )
        dinoParque1.añadirDino(dinoAñadido)
    else:
        idSeleccionado = int(opcion)
        if idSeleccionado < 0:
            eliminado = dinoParque1.eliminarDinobyID(abs(idSeleccionado))
            if eliminado:
                print("Dino eliminado correctamente.")
            else:
                print("No existe un dino con ese ID.")
        elif idSeleccionado > 0:
            dinoSeleccionado = None
            for d in dinoParque1.DinosHabitantes:
                if d.idDino == idSeleccionado:
                    dinoSeleccionado = d
                    break
            if dinoSeleccionado is None:
                print("No existe un dino con ese ID.")
            else:
                print("\nDino seleccionado:")
                print(dinoSeleccionado)
                while True:
                    print("\n¿Qué quieres modificar?")
                    print("1 - Nombre")
                    print("2 - Altura")
                    print("3 - Peso")
                    print("4 - Habilidades")
                    print("0 - Volver")
                    campo = input("Selecciona campo: ")
                    if campo == "1":
                        dinoSeleccionado.nombre = input("Nuevo nombre: ")
                    elif campo == "2":
                        dinoSeleccionado.altura = float(input("Nueva altura: "))
                    elif campo == "3":
                        dinoSeleccionado.peso = float(input("Nuevo peso: "))
                    elif campo == "4":
                        nuevasHab = input("Habilidades separadas por comas: ")
                        dinoSeleccionado.habilidades = nuevasHab.split(",")
                    elif campo == "0":
                        break
                    else:
                        print("Opción inválida.")
    if opcion == "S":
        break
