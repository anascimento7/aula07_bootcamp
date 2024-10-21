from typing import Dict, List
import csv

def ler_csv(nome_arquivo_csv: str) -> List[Dict]:
    """
    Função que lê um arquivo csv e retorna uma lista de dicionários
    """
    lista = []
    with open(nome_arquivo_csv, mode='r',encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return list(lista)


def filtrar_produtos_nao_entregues(produtos: list[dict]) -> list[dict]:
    """
    Função que filtra produtos onde entrega = True
    """
    lista_com_produtos_filtrados = []
    for produto in produtos:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados


def somar_valores_produtos(lista_produtos: list[dict]) -> int:
    """
    Função para somar valores dos produtos de uma lista
    """
    valor_total = 0
    for produto in lista_produtos:
        valor_total += int(produto.get("price"))
    return valor_total
