from pathlib import Path

import pandas as pd

pasta_arquivo = Path(__file__).resolve().parents[1]

arquivo_excel = pasta_arquivo / 'data' / 'raw' / 'Bahia_2025.xlsx'

if not arquivo_excel.exists():
    raise FileNotFoundError(
        f'Arquivo não encontrado: {arquivo_excel}'
    )

with pd.ExcelFile(arquivo_excel) as excel:
    print(f'Planilhas não encontradas: {excel.sheet_names}')

    for nome_planilha in excel.sheet_names:
        df = pd.read_excel(excel, sheet_name=nome_planilha)

        print('\n' + '=' * 70)
        print(f'Planilha: {nome_planilha}')
        print('=' * 70)

        print(f"Quantidade de linhas: {df.shape[0]}")
        print(f"Quantidade de colunas: {df.shape[1]}")

        print("\nNomes das colunas:")
        print(df.columns.tolist())

        print("\nPrimeiras cinco linhas:")
        print(df.head().to_string())

        print("\nTipos identificados pelo pandas:")
        print(df.dtypes)

        print("\nQuantidade de valores nulos por coluna:")
        print(df.isna().sum())

        print("\nQuantidade de linhas totalmente duplicadas:")
        print(df.duplicated().sum())

        print("\nResumo técnico:")
        df.info()



