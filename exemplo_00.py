#Calcular Média de Valores em uma Lista

from typing import List

#def calcular_valores_lista(valores: List[int]) -> float:
#    media: float = sum(valores) / len(valores)
#    return media

#lista_teste = [3,5,10,11]

#print(calcular_valores_lista(lista_teste))

# Filtrar Dados Acima de um Limite

#def filtrar_dados_acima_limite(limite: float, valores: List[float]) -> float:
#    lista_valores = []
#    for valor in valores:
#        if valor > limite:
#            lista_valores.append(valor)
#    return lista_valores


#teste_valores = [15,13,14,6,8,2,3,4]
#limite = 3

#print(filtrar_dados_acima_limite(limite, teste_valores))

# Contar Valores Únicos em uma Lista

#def contar_valores_lista(lista: List[int]) -> int:
#    return len(set(lista))

#testando_valores = [10,10,3,3,1,2,3,4,5,6,6]

#print(contar_valores_lista(testando_valores))

# Converter Celsius para Fahrenheit em uma Lista

#def celsius_to_farenheit(temp_celsius: List[float]) -> List[float]:
#    return [temp * (9/5) + 32 for temp in temp_celsius]

#lista_temp = [32.5,22.5,33.9,38]

#print(celsius_to_farenheit(lista_temp))