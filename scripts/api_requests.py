"""
Este módulo contém funções para interagir com a API da Receita Federal. 
As funções disponíveis são:

- `get_company_data`: realiza uma consulta à API usando um CNPJ específico, 
  retornando os dados da empresa ou um erro em caso de falha.

- `get_all_data`: obtém dados de várias empresas a partir de uma lista de CNPJs,
  tratando o erro 429 e aguardando um minuto antes de tentar novamente.

Autor: Gabriel Costa
Data de Criação: 19/10/2024
"""
import requests
from tqdm import tqdm
import time
from spinner import show_spinner

def get_company_data(cnpj: str) -> dict:
    """
    Obtém dados da empresa a partir do CNPJ usando a ReceitaWS.

    O CNPJ é formatado para remover caracteres especiais (ponto, barra, hífen) antes de ser utilizado na consulta.

    Parâmetros:
    ----------
    cnpj : str
        O CNPJ da empresa a ser consultado, que pode incluir caracteres especiais.

    Retorna:
    -------
    dict
        Um dicionário contendo os dados da empresa se a consulta for bem-sucedida, 
        ou None em caso de falha na consulta.

    Levanta:
    -------
    requests.exceptions.HTTPError
        Se a resposta da API indicar um erro de HTTP.
    """
    # Remove caracteres especiais do CNPJ
    cnpj = (cnpj.replace('.', '')
                .replace('/', '')
                .replace('-', ''))

    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro se o status da resposta não for 200
        return response.json()  # Retorna os dados da empresa como um dicionário
    
    except requests.exceptions.HTTPError as http_err:
        print(f'Houve um erro HTTP. Erro: {http_err}')
        
    except Exception as e:
        print(f'Houve um erro: {e}')

    return None


def get_all_data(lista_cnpj: list) -> list:
    """
    Obtém dados de várias empresas a partir de uma lista de CNPJs.

    Para cada CNPJ, faz uma consulta à API e trata o erro 429, 
    esperando um minuto antes de tentar novamente.

    Parâmetros:
    ----------
    lista_cnpj : list
        Uma lista de CNPJs a serem consultados.

    Retorna:
    -------
    list
        Uma lista de dicionários contendo os dados das empresas.
    """
    companies_data = []  # Lista para armazenar os dados das empresas
    total_cnpjs = len(lista_cnpj)  # Total de CNPJs a serem consultados
    
    # Usando tqdm para a barra de progresso
    for index, cnpj in tqdm(enumerate(lista_cnpj), total=total_cnpjs, desc="Consultando CNPJs"):
        while True:  # Loop para garantir que tentaremos novamente se recebermos erro 429
            company_data = get_company_data(cnpj)

            if company_data is not None:
                companies_data.append(company_data)  # Adiciona os dados à lista
                break  # Sai do loop se a consulta foi bem-sucedida
            else:
                # Verifica se o erro foi 429
                remaining_cnpjs = total_cnpjs - (index + 1)  # CNPJs restantes
                print(f"Erro ao buscar CNPJ {cnpj}. Tentando novamente após 1 minuto... {remaining_cnpjs} CNPJ(s) restante(s).")

                # Inicia o spinner por 60 segundos
                show_spinner(60)

                print()  # Nova linha após o spinner
                time.sleep(1)  # Breve pausa após o spinner para evitar múltiplas impressões de linha

    return companies_data
