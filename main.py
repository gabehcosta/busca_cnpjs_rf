"""
Este é o módulo principal do projeto de automação para busca de CNPJs na Receita Federal. 
O programa extrai uma lista de CNPJs de um arquivo Excel, consulta os dados das empresas 
usando a API da Receita Federal e exibe os resultados no console. 
Além disso, trata os erros da API, incluindo a limitação de requisições.

Autor: Gabriel Costa
Data de Criação: 19/10/2024
"""
import pandas as pd
from scripts.data_extraction import extract_cnpjs_from_excel_file
from scripts.api_requests import get_all_data

def main() -> None:
    """
    Função principal do programa.

    Realiza a extração de uma lista de CNPJs de um arquivo Excel,
    consulta os dados das empresas usando a API da Receita Federal
    e exibe os resultados no console.

    Retorna:
    -------
    None
    """
    # Caminho do arquivo com a lista de CNPJs
    cnpjs_file_path = r'data\ListaCnpjs.xlsx'
    
    # Extraindo a lista de CNPJs do arquivo Excel
    lista_cnpjs = extract_cnpjs_from_excel_file(cnpjs_file_path)
    print('Lista de CNPJs:\n', lista_cnpjs, '\n')
    
    # Obtendo dados das empresas a partir da lista de CNPJs
    df_empresas = get_all_data(lista_cnpjs)
    print('Dados das empresas:\n', df_empresas)
    
    # Gerando o arquivo Excel com os dados das empresas
    df_empresas.to_excel('data/DadosEmpresas.xlsx', engine='openpyxl', index=False)
    
    # Gerando o arquivo CSV com os dados das empresas
    df_empresas.to_csv('data/DadosEmpresas.csv', index=False)
    

if __name__ == "__main__":
    main()
