from math import sqrt, ceil
from random import sample
from heapq import heappush, heappop

DISTANCIAS = []

def construir_estado_inicial(cidades):
  return sample(list(range(0, len(cidades))), len(cidades))

def calcular_valor(no):
  valor = 0
  for i in range(0, len(no) - 1):
    origem = no[i]
    destino = no[i+1]
    valor += DISTANCIAS[origem][destino]
  return valor

def escolher_sucessor(no_atual):
  estados = []
  
  for i in range(0, len(no_atual) - 1):
    estado_candidato = no_atual.copy()
    aux = estado_candidato[i + 1]
    estado_candidato[i + 1] = estado_candidato[i]
    estado_candidato[i] = aux
    heappush(estados, (calcular_valor(estado_candidato), estado_candidato))
    
  return heappop(estados)[1]

def subida_encosta(cidades):
  no_inicial = construir_estado_inicial(cidades)
  no_atual = no_inicial
  t = 0

  while True:
    proximo_no = escolher_sucessor(no_atual)
    delta_e = calcular_valor(proximo_no) - calcular_valor(no_atual)

    if delta_e >= 0:
      return [no_inicial, proximo_no]
    no_atual = proximo_no

    t += 1

def calcular_distancia(a, b):
  return ceil(sqrt((float(a[0]) - float(b[0]))**2 + (float(a[1]) - float(b[1]))**2))

def calcular_distancias(arquivo):
  f = open(arquivo)
  linhas = [line.rstrip() for line in f]
  f.close()
  cidades = [city.split(' ') for city in linhas]

  for cidade in cidades:
    distancias = []

    for destino in cidades:
      distancias.append(calcular_distancia([cidade[1], cidade[2]], [destino[1], destino[2]]))
    DISTANCIAS.append(distancias)

if __name__ == "__main__":
  calcular_distancias("uy734.tsp")
  lista_cidades = list(range(0, len(DISTANCIAS)))
  
  for i in range(1, 10):
    [inicio, fim] = subida_encosta(lista_cidades)
    print('-------------', 'EXECUÇÃO', i, '-------------',)
    print('------ PRIMEIRA ITERACAO -------')
    print('Percurso', [cidade + 1 for cidade in inicio])
    print('Distancia total', calcular_valor(inicio))
    print('------ ULTIMA ITERACAO -------')
    print('Percurso', [cidade + 1 for cidade in fim])
    print('Distancia total', calcular_valor(fim))
    print()