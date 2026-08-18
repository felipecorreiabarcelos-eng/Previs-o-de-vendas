"""
previsao.py

Responsável por treinar o modelo Prophet e gerar a previsão de vendas
para os próximos meses.
"""

from prophet import Prophet


def treinar_modelo(dados):
    """Cria e treina o modelo Prophet com o histórico de vendas."""

    modelo = Prophet(
        yearly_seasonality=True,   # considera padrões que se repetem no ano
        weekly_seasonality=True,   # considera padrões que se repetem na semana
        daily_seasonality=False
    )

    modelo.fit(dados)
    return modelo


def gerar_previsao(modelo, dias_para_prever=90):
    """Usa o modelo treinado para prever os próximos X dias."""

    futuro = modelo.make_future_dataframe(periods=dias_para_prever)
    previsao = modelo.predict(futuro)

    # yhat = valor previsto
    # yhat_lower / yhat_upper = intervalo de confiança (mínimo e máximo esperado)
    return previsao
