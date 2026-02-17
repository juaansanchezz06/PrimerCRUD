from Dino import Dino
from datetime import datetime
def getDatos(n:int) -> list[Dino]:

 return [

    Dino(1, "Tyrannosaurus Rex",
         ["Mandíbula poderosa", "Gran olfato"],
         4.0, 8000.0,
         True, False, False,
         datetime(1905, 1, 1),
         datetime(1990, 6, 15)
    ),

    Dino(2, "Triceratops",
         ["Cuernos defensivos", "Gran fuerza"],
         3.0, 6000.0,
         False, True, False,
         datetime(1889, 3, 1),
         datetime(1985, 4, 10)
    ),

    Dino(3, "Velociraptor",
         ["Gran velocidad", "Garras afiladas"],
         1.8, 15.0,
         True, False, False,
         datetime(1924, 5, 12),
         datetime(2001, 7, 20)
    ),

    Dino(4, "Brachiosaurus",
         ["Cuello largo", "Gran tamaño"],
         12.0, 50000.0,
         False, True, False,
         datetime(1903, 8, 1),
         datetime(1975, 9, 30)
    ),

    Dino(5, "Stegosaurus",
         ["Placas dorsales", "Cola con púas"],
         4.5, 7000.0,
         False, True, False,
         datetime(1877, 7, 1),
         datetime(1992, 11, 5)
    ),

    Dino(6, "Spinosaurus",
         ["Vela dorsal", "Hábil nadador"],
         5.0, 10000.0,
         True, False, False,
         datetime(1915, 2, 1),
         datetime(2008, 3, 18)
    ),

    Dino(7, "Ankylosaurus",
         ["Armadura corporal", "Maza en la cola"],
         2.0, 8000.0,
         False, True, False,
         datetime(1908, 4, 1),
         datetime(1980, 6, 22)
    ),

    Dino(8, "Gallimimus",
         ["Gran velocidad", "Ligereza"],
         2.5, 440.0,
         False, False, True,
         datetime(1963, 9, 15),
         datetime(1995, 1, 12)
    ),

    Dino(9, "Allosaurus",
         ["Dientes serrados", "Cazador ágil"],
         3.5, 2000.0,
         True, False, False,
         datetime(1877, 6, 1),
         datetime(2003, 5, 14)
    ),

    Dino(10, "Iguanodon",
         ["Pulgar en forma de espina", "Resistente"],
         3.0, 3500.0,
         False, True, False,
         datetime(1825, 2, 1),
         datetime(1970, 10, 10)
    )

]


'''
Cuando i de for = n , break for 
'''