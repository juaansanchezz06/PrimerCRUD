from Dino import Dino
from DinoParque import DinoParque
from datetime import datetime
from datos import getDatos

def imprimirListado(dinoParque: DinoParque):
    print("=== Listado de Dinos ===")
    for dino in dinoParque.DinosHabitantes:
        print(f"ID: {dino.idDino} | {dino.nombre} | {dino.peso}kg | {dino.altura}m")
    
    
def opciones():
    print("[ID] Ver / modificar")
    print("[O] Ordenar")
    print("[A] Añadir")
    print("[S] Salir")




