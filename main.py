import requests
import json


def autenticacao():
    cabecalho = {'Accept': 'application/json; version=3',
               'Authorization': 'Basic [XXXXXXX]'}
    requisicao = requests.post("https://api.azionapi.net/tokens", '', headers=cabecalho)
    x = json.loads(requisicao.text)
    print('Token: ' + x['token'])
    x = x["token"]
    return x


def listarEdgesApplications():
    pagina = 1
    ultimaPagina = 2
    resposta = None
    cabecalho = {
      'Accept': 'application/json; version=3',
      'Authorization': 'Token ' + autenticacao()
    }

    while pagina <= ultimaPagina:
        r = requests.get("https://api.azionapi.net/edge_applications?page=%s" % (pagina), headers=cabecalho)
        pagina = pagina + 1
        x = json.loads(r.text)
        ultimaPagina = x["total_pages"]
        if (resposta == None):
            resposta = json.dumps(x["results"])
        else:
            resposta = resposta + json.dumps(x["results"])

    print(resposta)
    return resposta

def buscarOrigins(edgeId, originId):
    cabecalho = {
        'Accept': 'application/json; version=3',
        'Authorization': 'Token ' + autenticacao()
    }

    r = requests.get(f"https://api.azionapi.net/edge_applications/{edgeId}/origins/{originId}", headers=cabecalho)
    x = json.loads(r.text)
    print(x)


def run():
    edges = listarEdgesApplications();
    edges_list = json.loads(edges.replace("][", ','))
    for json_edge in edges_list:
        edge_id = json_edge['id']
        edge_name = json_edge['name']
        if json_edge['origins'][0]['name'] == "Origin S3":
            origin_id = json_edge['origins'][1]['origin_id']
            print(str(edge_name) + ": " + str(edge_id) + " -> " + str(origin_id))
            buscarOrigins(edge_id, origin_id)


run()
