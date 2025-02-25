# Este código define uma variável nome e uma lista idades. Em seguida, adiciona uma nova idade à lista, calcula a média das idades e exibe os resultados. 

# Definindo uma variável
nome = "João"

# Definindo uma lista de idades
idades = [25, 30, 35, 40]

# Adicionando uma nova idade à lista
idades.append(45)

# Calculando a média das idades
media_idades = sum(idades) / len(idades)

# Exibindo os resultados
print(f"Nome: {nome}")
print(f"Idades: {idades}")
print(f"Média das idades: {media_idades:.2f}")