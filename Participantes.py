
class Participantes:
    def __init__(self, nombre, dni, auto, numero):
        self.nombre = nombre
        self.dni = dni
        self.auto = auto
        self.numero = numero

    def serialize(self):
        return {'nombre': self.nombre,
                'dni': self.dni,
                'auto': self.auto,
                'numero': self.numero
                }




