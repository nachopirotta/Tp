import json
from Tp.src.models.Carreras import Carreras


def cargar_carreras():
    carreras = []

    with open('Tp/src/db/carreras_mock.json', 'r') as file:
        carreras_json = json.load(file)
        for carrera in carreras_json:
            carreras.append(
                Carreras(
                    carrera['millas'],
                    carrera['horario'],
                    carrera['peso']
                )
            )
    return carreras


