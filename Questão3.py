"""Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, 
que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
"""

lista_faturamento = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]

def menor_faturamento(lista_faturamento):
    menor = lista_faturamento[0]["valor"]
    for i in lista_faturamento:
        if i["valor"] < menor:
            menor = i["valor"]
    return menor

def maior_faturamento(lista_faturamento):
    maior = lista_faturamento[0]["valor"]
    for i in lista_faturamento:
        if i["valor"] > maior:
            maior = i["valor"]
    return maior

def media_faturamento(lista_faturamento):
    soma = 0
    for i in lista_faturamento:
        soma += i["valor"]
    return soma / len(lista_faturamento)

def dias_acima_media(lista_faturamento):
    media = media_faturamento(lista_faturamento)
    dias = 0
    for i in lista_faturamento:
        if i["valor"] > media:
            dias += 1
    return dias

print(f"Menor faturamento: {menor_faturamento(lista_faturamento)}")
print(f"Maior faturamento: {maior_faturamento(lista_faturamento)}")
print(f"Média faturamento: {media_faturamento(lista_faturamento)}")
print(f"Dias acima da média: {dias_acima_media(lista_faturamento)}")