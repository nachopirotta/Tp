
import json
from flask import Flask, jsonify, request
from Tp.src.db.carga_participantes import cargar_participantes
from Tp.src.db.carga_carreras import cargar_carreras
from Tp.src.models.Participantes import Participantes
from Tp.src.models.Carreras import Carreras

app = Flask(__name__)



participantes: list = cargar_participantes()
carreras: list = cargar_carreras()
participantes1 = [part.serialize() for part in participantes]
carreras1 = [carr.serialize() for carr in carreras]

@app.route('/participantes', methods=['GET'])
def verParticipantes():
    return jsonify(participantes1)


@app.route('/carreras', methods=['GET'])
def verCarreras():
    return jsonify(carreras1)

@app.route('/participantes/<participante>', methods=['GET'])
def participanteGet(participante):
    for p in participantes1:
        if p["nombre"] == participante:
            return jsonify({'participante': p, "busqueda": participante, "status":"ok"})
    return jsonify({"busqueda": participante, "status": "not found"})


@app.route('/carreras/<carrera>', methods=['GET'])
def carreraGet(carrera):
    for c in carreras1:
        if c["millas"] == carrera:
            return jsonify({'carrera': c, "busqueda": carrera, "status": "ok"})
    return jsonify({"busqueda": carrera, "status": "not found"})


@app.route("/participantes", methods=['POST'])
def participantePost():
   part = request.json
   try:
       new_participante = Participantes(
           part['nombre'],
           part['auto'],
           part['dni'],
           part['numero']

       )
       participantes.append(new_participante)

   except KeyError as key_err:
       missing_param = (key_err.__str__())
       return jsonify(
           error_code="ERROR_BAD",
           error_description="Bad request",
           error_body=missing_param
       ), 400

   return jsonify(new_participante.serialize())

@app.route("/carreras", methods=['POST'])
def carreraPost():
    carrera = request.json
    try:
        new_carrera = Carreras(
            carrera['millas'],
            carrera['horario'],
            carrera['peso']


        )
        carreras.append(new_carrera)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="ERROR_BAD",
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(new_carrera.serialize())

@app.route('/participantes/<participante>', methods=['PUT'])
def participantePut(participante):
    body = request.json
    nombre = body["nombre"]
    auto = body["auto"]
    dni = body["dni"]
    numero = body["numero"]
    for indice, p in enumerate(participantes):
        if p.nombre == participante:
            return jsonify({"participante":  {"nombre": nombre, "auto": auto, "dni": dni, "numero": numero},"busqueda": participante, "status": "ok"})
    return jsonify({"busqueda": participante, "status": "not found"})

@app.route('/carreras/<carrera>', methods=['PUT'])
def carreraPut(carrera):
    body = request.json
    millas = body["millas"]
    horario = body["horario"]
    peso = body["peso"]
    for indice, c in enumerate(carreras):
        if c.millas == carrera:
            return jsonify({"carrera": {"millas": millas, "horario": horario, "peso": peso},"busqueda": carrera, "status": "ok"})
    return jsonify({"busqueda": carrera, "status": "not found"})

@app.route('/participantes/<participante>', methods=['DELETE'])
def participanteDelete(participante):
    for indice, p in enumerate(participantes1):
        if p["nombre"] == participante:
            participantes1[indice:indice+1] = []
            return jsonify({"participante": p,"busqueda": participante, "status": "ok"})
    return jsonify({"participantes": participantes1, "status": "not found"})

@app.route('/carreras/<carrera>', methods=['DELETE'])
def carreraDelete(carrera):
    for indice, c in enumerate(carreras1):
        if c["millas"] == carrera:
            carreras1[indice:indice+1] = []
            return jsonify({"carrera": c,"busqueda": carrera, "status": "ok"})
    return jsonify({"carreras": carreras1, "status": "not found"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)










