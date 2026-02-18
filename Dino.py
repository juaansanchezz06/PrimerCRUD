from datetime import datetime

class   Dino:
    def __init__(self, 
        idDino: int,
        nombre: str,
        habilidades: list[str],
        altura: float,
        peso:float,
        esCarnivoro: bool,
        esHerbivoro: bool,
        esOmnivoro: bool,
        FechaDescripcion: datetime,
        FechaEsqueletoCompleto: datetime
        ):
        self.idDino = idDino
        self.nombre = nombre
        self.habilidades = habilidades
        self.altura = altura
        self.peso = peso
        self.esCarnivoro = esCarnivoro
        self.esHerbivoro = esHerbivoro
        self.esOmnivoro = esOmnivoro
        self.fechaDescripcion = FechaDescripcion
        self.fechaEsqueletoCompleto = FechaEsqueletoCompleto
        
    def __eq__(self, other) -> bool:
        if isinstance(other, Dino):
            return self.idDino == other.idDino
        return False
    
    def __lt__(self, other) -> bool:
       return self.peso < other.peso

    def __hash__(self):
        return self.idDino

    def __le__(self, other) -> bool:
       return self.peso <= other.peso


    def __gt__(self, other) -> bool:
       return self.peso > other.peso


    def __ge__(self, other) -> bool:
       return self.peso >= other.peso

    def __str__(self):
       return (
           f"ID: {self.idDino}\n"
           f"Nombre: {self.nombre}\n"
           f"Habilidades: {self.habilidades}\n"
           f"Altura: {self.altura} m\n"
           f"Peso: {self.peso} N\n"
           f"Es Carnivoro: {self.esCarnivoro}\n"
           f"Es Herbivoro: {self.esHerbivoro}\n"
           f"Es Omnivoro: {self.esOmnivoro}\n"
           f"Fecha de descubrimiento: {self.fechaDescripcion}\n"
           f"Fecha en la que se completo su esqueleto: {self.fechaEsqueletoCompleto}\n"
       )
