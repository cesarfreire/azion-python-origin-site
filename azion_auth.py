import requests
import json


class AzionAuth:

    @staticmethod
    def autenticacao():
        cabecalho = {'Accept': 'application/json; version=3',
                   'Authorization': 'Basic XXXXXXXX'}
        requisicao = requests.post("https://api.azionapi.net/tokens", '', headers=cabecalho)
        token = json.loads(requisicao.text)
        print('Token: ' + token['token'])
        token = token["token"]
        return token