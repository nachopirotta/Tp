# API DE TERCEROS

import requests
url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/postas-de-vacunacion-covid-19/postas_vacunacion_covid.geojson'


response = requests.get(url)


vacunacion_api = (response.json())

vacunaciones = []


for vacunacion in vacunacion_api["features"]:

    postas_vacunacion = ("categoria" == vacunacion['properties']["categoria"],
                         "direccion" == vacunacion['properties']["direccion"],
                         "barrio" == vacunacion['properties']["barrio"])



    vacunaciones.append(postas_vacunacion)