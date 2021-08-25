from math import exp, sqrt, ceil
from random import choice, random, sample

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
    estados.append(estado_candidato)
    
  return choice(estados)

def tempera_simulada(cidades):
  no_inicial = construir_estado_inicial(cidades)
  no_atual = no_inicial
  t = 0
  T = 500

  while True:
    proximo_no = escolher_sucessor(no_atual)
    delta_e = calcular_valor(proximo_no) - calcular_valor(no_atual)

    if T <= 0:
      return [no_inicial, proximo_no]
    elif delta_e < 0:
      no_atual = proximo_no
    elif random() <= exp(-delta_e / T):
      no_atual = proximo_no
      
    print(calcular_valor(no_atual))
     
    T -= 0.075
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
  
  [inicio, fim] = tempera_simulada(lista_cidades)
  print('------ PRIMEIRA ITERACAO -------')
  print('Percurso', [cidade + 1 for cidade in inicio])
  print('Distancia total', calcular_valor(inicio))
  print('------ ULTIMA ITERACAO -------')
  print('Percurso', [cidade + 1 for cidade in fim])
  print('Distancia total', calcular_valor(fim))
  print()