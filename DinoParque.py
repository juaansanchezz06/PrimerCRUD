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
    
    def añadirDino(self, dino: Dino) -> None:
        self.DinosHabitantes.append(dino)

    def eliminarDinobyID(self, idDino: int) -> bool:
        for Dino in self.DinosHabitantes:
            if Dino.idDino == idDino:
                self.DinosHabitantes.remove(Dino)
                return True
        return False
    
    def vaciarParque(self):
        return self.DinosHabitantes.clear()
    def alimentarDino(self , idDino: int ,cantidad: int)-> None:
        alimento = cantidad * 100
        for Dino in self.DinosHabitantes:
            if Dino.idDino == idDino:
                Dino.peso += alimento
    def masGordo():
        pass
    def masDelgado():
        pass
    def PrimerDescubierto():
        pass
    def ultimoDescubierto():
        pass

    def __str__(self) -> str:
        res = f"DinoParque #{self.idDinoParque}\n"
        res += f"Nombre: {self.nombreDinoParque}\n"
        res += "Dinos en dinoparque:\n"
        for dino in self.DinosHabitantes:
            res += f"#{dino.idDino} -- {dino.nombre} -- ({dino.peso}kg)\n" 
        return res  
    