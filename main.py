url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
ur = " "

# Sanitização da URL
url = url.replace(" ", "") # serve para substituir caracteres de uma string por outro

#validação da URL
if url == "":
    raise ValueError("A URL está vazia")

# Separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:indice_e_comercial]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)