from Dino import Dino
from DinoParque import DinoParque
from datetime import datetime
from datos import getDatos

dinos1 = getDatos(0)
dinos2 = getDatos(1)
dinos3 = getDatos(2)
megalodon = Dino(
    222,
    "Megalodon",
    ["Mandíbula extremadamente poderosa",
    "Gran velocidad en el agua",
    "Depredador ápice"
    ],
    18,
    50000.,
    True,
    False,
    False,
    datetime(1843, 1, 1),
    datetime(1909, 1, 1)
)


print("Listado Completo")
dinoParque1 = DinoParque(1, "Rocoso", dinos1)
print(dinoParque1)

print("Probando eliminar...")
DinoParque.eliminarDinobyID(dinoParque1, 1)
print(dinoParque1)

print("Probando a añadir")
DinoParque.añadirDino(dinoParque1, megalodon)
print(dinoParque1)

print("Probando vaciar dino Parque")
DinoParque.vaciarParque(dinoParque1)
print(dinoParque1)

print("Probando dinoParque2")
dinoParque2 = DinoParque(2, "Mixto", dinos2)
print(dinoParque2)

print("Probando alimentar dinos")
DinoParque.alimentarDino(dinoParque2, 12, 5)
print(dinoParque2)

print("Probando dino mas gordo")
masGordo = DinoParque.masGordo(dinoParque2)
print(masGordo)

print("Probando dino mas delgado")
masDelgado = DinoParque.masDelgado(dinoParque2)
print(masDelgado)

print("Probando primer descubierto")
primerDescubierto = DinoParque.PrimerDescubierto(dinoParque2)
print(primerDescubierto)

print("Probando dino mas delgado")
ultimoDescubierto = DinoParque.ultimoDescubierto(dinoParque2)
print(ultimoDescubierto)

