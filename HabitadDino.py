from Dino import Dino

class HabitadDino:
    def __init__(
        self,
        idHabitadDino: int,
        nombreHabitad: str,
        DinosHabitantes: list[Dino] | None = None
    ):
        self.idHabitadDino = idHabitadDino
        self.nombreHabitad = nombreHabitad
        self.DinosHabitantes = DinosHabitantes

        if DinosHabitantes is None:
            self.DinosHabitantes: list[Dino] = []
        else:
            self.DinosHabitantes = DinosHabitantes

    
    def añadirDino(self, Dino: Dino) -> None:
        self.DinosHabitantes.append(Dino)

    def eliminarDinobyID(self, idDino: str) -> bool:
        for Dino in self.DinosHabitantes:
            if Dino.idDino == idDino:
                self.DinosHabitantes.remove(Dino)
                return True
        return False
    
    def pesoLunar():
        pass    
    def cambioDieta():
        pass
    def masGordo():
        pass
    def masDelgado():
        pass
    def PrimerDescubierto():
        pass
    def PrimerEsqueletoCompleto():
        pass