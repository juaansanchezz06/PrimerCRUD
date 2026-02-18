from Dino import Dino

class DinoParque:
    def __init__(
        self,
        idDinoParque: int,
        nombreDinoParque: str,
        DinosHabitantes: list[Dino] | None = None
    ):
        self.idDinoParque = idDinoParque
        self.nombreDinoParque = nombreDinoParque
        self.DinosHabitantes = DinosHabitantes

        if DinosHabitantes is None:
            self.DinosHabitantes: list[Dino] = []
        else:
            self.DinosHabitantes = DinosHabitantes
    def __hash__(self):
        return self.idDinoParque        
    
    def añadirDino(self, Dino: Dino) -> None:
        self.DinosHabitantes.append(Dino)

    def eliminarDinobyID(self, idDino: int) -> bool:
        for Dino in self.DinosHabitantes:
            if Dino.idDino == idDino:
                self.DinosHabitantes.remove(Dino)
                return True
        return False
    
    def pesoLunar(self):

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

    def __str__(self) -> str:
        res = f"DinoParque #{self.idDinoParque}\n"
        res += f"Nombre: {self.nombreDinoParque}\n"
        res += "Dinos en dinoparque:\n"
        for dino in self.DinosHabitantes:
            res += f"#{dino.idDino} -- {dino.nombre}\n" 
        return res  
    