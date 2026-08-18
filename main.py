"""
main.py

Trabalho: Sistema de Previsão de Vendas
Faculdade: Estácio
Curso: Ciência da Computação - 3º período
Aluno: [coloque seu nome aqui]

Objetivo do sistema:
1) Analisar o histórico de vendas de um ano
2) Identificar tendências futuras
3) Gerar um gráfico com a projeção de vendas

Bibliotecas usadas: pandas e prophet

Este arquivo apenas chama as funções dos outros módulos,
para deixar o projeto organizado.
"""

from gerar_dados import gerar_dados_exemplo
from previsao import treinar_modelo, gerar_previsao
from graficos import gerar_grafico_previsao, gerar_grafico_componentes


def main():
    # 1) Carregar/gerar os dados de vendas
    dados = gerar_dados_exemplo()
    print("Amostra do histórico de vendas:")
    print(dados.head())
    print(f"\nTotal de registros: {len(dados)}")

    # 2) Treinar o modelo
    modelo = treinar_modelo(dados)
    print("\nModelo treinado com sucesso!")

    # 3) Gerar a previsão
    previsao = gerar_previsao(modelo, dias_para_prever=90)
    print("\nPrevisão para os próximos dias:")
    print(previsao[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(10))

    # 4) Gerar os gráficos
    gerar_grafico_previsao(modelo, previsao)
    gerar_grafico_componentes(modelo, previsao)


if __name__ == "__main__":
    main()
