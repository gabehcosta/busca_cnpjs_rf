import pandas as pd

def save_to_excel(df: pd.DataFrame, file_name: str) -> None:
    """
    Salva os dados do DataFrame em um arquivo Excel.

    Parâmetros:
    ----------
    df : pd.DataFrame
        O DataFrame a ser salvo.

    file_name : str
        O nome do arquivo Excel (deve terminar com .xlsx).

    Retorno:
    -------
    None
        Esta função não retorna nenhum valor.
    """
    try:
        df.to_excel(file_name, index=False)  # Salva o DataFrame no Excel sem o índice
        print(f"Arquivo '{file_name}' salvo com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
