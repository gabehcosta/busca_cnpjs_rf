# Busca CNPJs RF

Ferramenta para buscar e analisar dados de CNPJs a partir das informações públicas disponibilizadas pela Receita Federal.

## Descrição

Este projeto permite a consulta e análise de dados cadastrais de empresas brasileiras utilizando o Cadastro Nacional da Pessoa Jurídica (CNPJ) fornecido pela Receita Federal. É especialmente útil para analistas de dados e engenheiros de dados que necessitam manipular e extrair insights dessas informações.

## Funcionalidades

- **Consulta de CNPJs**: Pesquise informações detalhadas sobre empresas pelo número do CNPJ.
- **Exportação de Resultados**: Exporte os dados consultados para formatos como CSV ou XLSX para uso posterior.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas Python:
  - `requests`
  - `pandas`

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/gabehcosta/busca_cnpjs_rf.git
   ```

2. **Navegue até o diretório do projeto**:

   ```bash
   cd busca_cnpjs_rf
   ```

3. **Crie um ambiente virtual**:

   ```bash
   python3 -m venv venv
   ```

4. **Ative o ambiente virtual**:

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Preparação dos Dados**: Certifique-se de ter um arquivo excel como o do reposítorio, contendo apenas os CNPJs das empresas que deseja realizar a busca.

2. **Execução do Script Principal**: Utilize o script `main.py` localizado no diretório raiz para iniciar as consultas. Por exemplo:

   ```bash
   python .\main.py
   ```

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
