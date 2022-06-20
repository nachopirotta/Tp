# CARGA DE PARTICIPANTES

import json
from Tp.src.models.Participantes import Participantes


def cargar_participantes():
    participantes = []

    with open('Tp/src/db/participantes_mock.json', 'r') as file:
        participantes_json = json.load(file)
        for participante in participantes_json:
            participantes.append(
                Participantes(
                    participante['nombre'],
                    participante['dni'],
                    participante['auto'],
                    participante['numero']
                )
            )
    return participantes
