"""
Este módulo contém funções para extrair dados de arquivos Excel. 
Especificamente, a função `extract_cnpjs_from_excel_file` lê um arquivo Excel 
e retorna uma lista de CNPJs únicos extraídos da coluna especificada.

Autor: Gabriel Costa
Data de Criação: 19/10/2024
"""
import pandas as pd

def extract_cnpjs_from_excel_file(excel_file_path: str) -> list:
    """
    Extrai uma lista de CNPJs de um arquivo Excel.

    Parâmetros:
    ----------
    excel_file_path : str
        O caminho para o arquivo Excel a ser lido.

    Retorna:
    -------
    list
        Uma lista de CNPJs únicos extraídos da coluna A da planilha 'ListaCnpjs'.
    
    Levanta:
    -------
    FileNotFoundError
        Se o arquivo especificado não for encontrado.
    ValueError
        Se a planilha 'ListaCnpjs' ou a coluna A não estiverem presentes no arquivo.
    """
    # Lê a coluna A da planilha 'ListaCnpjs'
    cnpjs = pd.read_excel(excel_file_path, engine='openpyxl', usecols='A', sheet_name='ListaCnpjs')
    
    # Droppa duplicatas
    cnpjs = cnpjs.drop_duplicates()
    
    # Retorna a primeira coluna como uma lista
    return cnpjs.iloc[:, 0].tolist()
