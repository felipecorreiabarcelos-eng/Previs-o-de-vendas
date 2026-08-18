"""
gerar_dados.py

Responsável por criar/carregar o histórico de vendas.
Na vida real, aqui você trocaria pela leitura de um CSV:

    dados = pd.read_csv("dados/vendas.csv")

O Prophet exige que as colunas se chamem "ds" (data) e "y" (valor).
"""

import numpy as np
import pandas as pd


def gerar_dados_exemplo():
    """Gera um histórico de vendas fictício de 1 ano (dia a dia)."""

    datas = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")

    np.random.seed(42)  # trava o "aleatório" pra sempre dar o mesmo resultado

    tendencia = np.linspace(100, 300, len(datas))               # vendas crescendo aos poucos
    sazonalidade = 20 * np.sin(np.linspace(0, 12 * np.pi, len(datas)))  # oscilação
    ruido = np.random.normal(0, 10, len(datas))                 # variação do dia a dia

    vendas = tendencia + sazonalidade + ruido
    vendas = vendas.clip(min=0)  # vendas não podem ser negativas

    df = pd.DataFrame({"ds": datas, "y": vendas})
    return df


if __name__ == "__main__":
    # Permite rodar este arquivo sozinho para conferir os dados gerados
    dados = gerar_dados_exemplo()
    print(dados.head())
    print(f"\nTotal de registros: {len(dados)}")

    # Salva em CSV para poder ser reaproveitado depois
    dados.to_csv("dados/vendas.csv", index=False)
    print("\nArquivo 'dados/vendas.csv' gerado com sucesso!")
