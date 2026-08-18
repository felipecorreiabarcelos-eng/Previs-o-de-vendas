"""
graficos.py

Responsável por gerar e salvar os gráficos de projeção de vendas.
"""

import matplotlib.pyplot as plt


def gerar_grafico_previsao(modelo, previsao, caminho="graficos/previsao_vendas.png"):
    """Gera o gráfico principal com a linha de previsão e o intervalo de confiança."""

    fig = modelo.plot(previsao)
    plt.title("Previsão de Vendas - Próximos 90 dias")
    plt.xlabel("Data")
    plt.ylabel("Vendas")
    plt.tight_layout()
    plt.savefig(caminho)
    print(f"Gráfico salvo em '{caminho}'")


def gerar_grafico_componentes(modelo, previsao, caminho="graficos/componentes_previsao.png"):
    """Gera o gráfico separando tendência e sazonalidade."""

    fig = modelo.plot_components(previsao)
    plt.tight_layout()
    plt.savefig(caminho)
    print(f"Gráfico salvo em '{caminho}'")
