from math import sqrt

def construir_estado_inicial(cidades):
  pass

def calcular_temperatura(t):
  pass

def escolher_sucessor(no_atual):
  pass

def calcular_valor(no):
  pass

def probabilidade_aleatoria():
  pass

def calcular_probabilidade_no(delta_e, T):
  pass

def tempera_simulada(cidades):
  no_atual = construir_estado_inicial(cidades)
  t = 0

  while True:
    T = calcular_temperatura(t)
    
    if T == 0:
      return no_atual

    proximo_no = escolher_sucessor(no_atual)
    delta_e = calcular_valor(proximo_no) - calcular_valor(no_atual)

    if delta_e > 0:
      no_atual = proximo_no
    elif probabilidade_aleatoria() < calcular_probabilidade_no(delta_e, T):
      no_atual = proximo_no

    t += 1

def calcular_distancia(a, b):
  return sqrt((float(a[0]) - float(b[0]))**2 + (float(a[1]) - float(b[1]))**2)

def calcular_distancias(arquivo):
  matriz_distancias = []

  f = open(arquivo)
  linhas = [line.rstrip() for line in f]
  f.close()
  cidades = [city.split(' ') for city in linhas]

  for cidade in cidades:
    distancias = []

    for destino in cidades:
      distancias.append(calcular_distancia([cidade[1], cidade[2]], [destino[1], destino[2]]))

    matriz_distancias.append(distancias)

  return matriz_distancias

if __name__ == "__main__":
  matriz_distancias = calcular_distancias("dj38.tsp")
  tempera_simulada([])
