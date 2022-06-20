class Carreras:
    def __init__(self, millas, horario, peso):
        self.millas = millas
        self.horario = horario
        self.peso = peso

    def serialize(self):
        return {'millas': self.millas,
                'horario': self.horario,
                'peso': self.peso,
                }


class Carrera_un_cuarto_milla(Carreras):
    def __init__(self, millas, horario, peso):
        super().__init__(millas, horario, peso)

class Carrera_media_milla(Carreras):
    def __init__(self, millas, horario, peso):
        super().__init__(millas, horario, peso)

class Carrera_una_milla(Carreras):
    def __init__(self, millas, horario, peso):
        super().__init__(millas, horario, peso)