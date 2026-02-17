from Dino import Dino
from datetime import datetime
def getDatos(n:int) -> list[Dino]:
     matrizDinos = [
          [
               Dino(1, "Tyrannosaurus Rex", ["mordida poderosa", "gran olfato"], 4.0, 8000.0, True, False, False, datetime(1905, 1, 1), datetime(1990, 6, 15)),
               Dino(2, "Velociraptor", ["velocidad", "inteligencia"], 1.8, 15.0, True, False, False, datetime(1924, 1, 1), datetime(1980, 5, 10)),
               Dino(3, "Spinosaurus", ["gran tamaño", "habilidad acuática"], 4.5, 7500.0, True, False, False, datetime(1915, 1, 1), datetime(2005, 4, 18)),
               Dino(4, "Allosaurus", ["garras afiladas", "cazador ágil"], 3.5, 2000.0, True, False, False, datetime(1877, 1, 1), datetime(1988, 2, 14)),
               Dino(5, "Carnotaurus", ["cuernos frontales", "gran velocidad"], 3.0, 1500.0, True, False, False, datetime(1985, 1, 1), datetime(1992, 11, 3)),
               Dino(6, "Giganotosaurus", ["gran tamaño", "depredador dominante"], 4.2, 8200.0, True, False, False, datetime(1995, 1, 1), datetime(1999, 6, 25)),
               Dino(7, "Carcharodontosaurus", ["dientes afilados", "gran mordida"], 4.0, 6000.0, True, False, False, datetime(1931, 1, 1), datetime(2001, 9, 12)),
               Dino(8, "Albertosaurus", ["rapidez", "caza en grupo"], 3.3, 2500.0, True, False, False, datetime(1905, 1, 1), datetime(1978, 4, 3)),
               Dino(9, "Dilophosaurus", ["doble cresta", "agilidad"], 2.5, 400.0, True, False, False, datetime(1954, 1, 1), datetime(1987, 8, 19)),
               Dino(10, "Majungasaurus", ["cráneo robusto", "resistencia"], 2.8, 1100.0, True, False, False, datetime(1896, 1, 1), datetime(1996, 10, 7))
          ],
          [
               Dino(11, "Triceratops", ["cuernos defensivos", "gran resistencia"], 3.0, 6000.0, False, True, False, datetime(1889, 1, 1), datetime(2000, 3, 20)),
               Dino(12, "Stegosaurus", ["placas óseas", "cola con púas"], 4.5, 5000.0, False, True, False, datetime(1877, 1, 1), datetime(1995, 7, 12)),
               Dino(13, "Brachiosaurus", ["cuello largo", "gran altura"], 12.0, 35000.0, False, True, False, datetime(1903, 1, 1), datetime(1998, 6, 9)),
               Dino(14, "Diplodocus", ["cola larga", "gran tamaño"], 8.0, 15000.0, False, True, False, datetime(1878, 1, 1), datetime(1991, 10, 22)),
               Dino(15, "Ankylosaurus", ["armadura ósea", "mazo en la cola"], 2.0, 8000.0, False, True, False, datetime(1908, 1, 1), datetime(1984, 5, 17)),
               Dino(16, "Iguanodon", ["pulgar puntiagudo", "herbívoro robusto"], 3.5, 3500.0, False, True, False, datetime(1825, 1, 1), datetime(1975, 2, 6)),
               Dino(17, "Parasaurolophus", ["cresta sonora", "vida en manada"], 4.0, 2500.0, False, True, False, datetime(1922, 1, 1), datetime(1981, 11, 14)),
               Dino(18, "Hadrosaurus", ["pico ancho", "gran resistencia"], 2.5, 3000.0, False, True, False, datetime(1858, 1, 1), datetime(1993, 5, 8)),
               Dino(19, "Corythosaurus", ["cresta prominente", "comunicación sonora"], 3.0, 2800.0, False, True, False, datetime(1914, 1, 1), datetime(1989, 6, 30)),
               Dino(20, "Kentrosaurus", ["espinas dorsales", "cola defensiva"], 2.0, 1000.0, False, True, False, datetime(1915, 1, 1), datetime(1979, 9, 2))
          ],
          [
               Dino(21, "Oviraptor", ["protección de huevos", "agilidad"], 1.5, 33.0, False, False, True, datetime(1924, 1, 1), datetime(1976, 8, 30)),
               Dino(22, "Gallimimus", ["gran velocidad", "visión aguda"], 2.0, 440.0, False, False, True, datetime(1963, 1, 1), datetime(1985, 9, 5)),
               Dino(23, "Therizinosaurus", ["garras enormes", "alcance extendido"], 5.0, 5000.0, False, False, True, datetime(1954, 1, 1), datetime(1993, 7, 1)),
               Dino(24, "Ornithomimus", ["rapidez", "ligereza"], 1.8, 170.0, False, False, True, datetime(1890, 1, 1), datetime(1982, 4, 11)),
               Dino(25, "Plateosaurus", ["cuello flexible", "dieta variada"], 3.5, 4000.0, False, False, True, datetime(1837, 1, 1), datetime(1970, 12, 25)),
               Dino(26, "Pachycephalosaurus", ["cráneo grueso", "defensa craneal"], 1.5, 450.0, False, False, True, datetime(1943, 1, 1), datetime(1980, 3, 16)),
               Dino(27, "Microraptor", ["plumas", "planeo"], 0.8, 1.0, True, False, True, datetime(2000, 1, 1), datetime(2003, 5, 21)),
               Dino(28, "Struthiomimus", ["gran velocidad", "cuerpo ligero"], 1.4, 150.0, False, False, True, datetime(1917, 1, 1), datetime(1990, 4, 27)),
               Dino(29, "Segnosaurus", ["garras largas", "alimentación variada"], 4.0, 3000.0, False, False, True, datetime(1979, 1, 1), datetime(1995, 8, 13)),
               Dino(30, "Erlikosaurus", ["pico fuerte", "movilidad ágil"], 3.4, 2000.0, False, False, True, datetime(1980, 1, 1), datetime(1992, 6, 6))
          ]
          ]
     listaDinos = []
     for dino in matrizDinos[n]:
          listaDinos.append(dino)
     return listaDinos
      




