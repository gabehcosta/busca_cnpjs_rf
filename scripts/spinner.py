"""
Este módulo contém funções auxiliares para exibir um spinner no terminal, 
indicando que uma operação está em andamento. 
A função `show_spinner` exibe um spinner por um período específico, 
e `spinning_cursor` gera a sequência de caracteres do spinner.

Autor: Gabriel Costa
Data de Criação: 19/10/2024
"""
import sys
import time

def spinning_cursor():
    """Gerador para criar um spinner em movimento."""
    while True:
        for cursor in '|/-\\':
            yield cursor

def show_spinner(duration: int) -> None:
    """
    Exibe um spinner no terminal durante um período especificado.

    Parâmetros:
    ----------
    duration : int
        Duração em segundos para mostrar o spinner.
    """
    spinner = spinning_cursor()
    end_time = time.time() + duration  # Tempo de término
    while time.time() < end_time:
        sys.stdout.write(next(spinner))  # Imprime o próximo caractere do spinner
        sys.stdout.flush()  # Força a impressão no terminal
        time.sleep(0.2)  # Espera 0.2 segundo, isso que gera o efeito de giro do spinner
        sys.stdout.write('\b')  # Apaga o caractere anterior
