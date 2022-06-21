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

