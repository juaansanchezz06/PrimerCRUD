from datetime import datetime

class   Dino:
    def __init__(self, 
        idDino: int,
        nombre: str,
        habilidades: list[str],
        alturaMedia: float,
        pesoMedio:float,
        esCarnivoro: bool,
        esHerbivoro: bool,
        esOmnivoro: bool,
        FechaDescripcion: datetime,
        FechaEsqueletoCompleto: datetime
        ):
        self.idDino = idDino
        self.nombre = nombre
        self.habilidades = habilidades
        self.alturaMedia = alturaMedia
        self.pesoMedio = pesoMedio
        self.esCarnivoro = esCarnivoro
        self.esHerbivoro = esHerbivoro
        self.esOmnivoro = esOmnivoro
        self.fechaDescripcion = FechaDescripcion
        self.fechaEsqueletoCompleto = FechaEsqueletoCompleto
        
    def __eq__(self, other) -> bool:
        if isinstance(other, Dino):
            return self.idDino == other.idDino
        return False
    
    
    def __str__(self):
       return (
           f"Título: {self.idDino}\n"
           f"Título: {self.nombre}\n"
           f"Título: {self.habilidades}\n"
           f"Título: {self.alturaMedia}\n"
           f"Título: {self.pesoMedio}\n"
           f"Título: {self.esCarnivoro}\n"
           f"Título: {self.esHerbivoro}\n"
           f"Título: {self.esOmnivoro}\n"
           f"Título: {self.fechaDescripcion}\n"
           f"Título: {self.fechaEsqueletoCompleto}\n"
       )
