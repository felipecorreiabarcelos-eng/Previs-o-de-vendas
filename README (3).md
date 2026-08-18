# 📈 Previsão de Vendas

Trabalho da faculdade Estácio — Ciência da Computação, 3º período.

Sistema simples que:
- analisa o histórico de vendas de um ano;
- identifica tendências futuras;
- gera um gráfico de projeção.

## 🛠️ Bibliotecas usadas
- [pandas](https://pandas.pydata.org/)
- [prophet](https://facebook.github.io/prophet/)
- matplotlib
- numpy

## 📂 Estrutura do projeto

```
previsao-vendas/
├── main.py               # arquivo principal, roda tudo
├── gerar_dados.py         # cria/carrega o histórico de vendas
├── previsao.py             # treina o modelo e gera a previsão
├── graficos.py              # gera e salva os gráficos
├── dados/                    # onde fica o CSV com o histórico
├── graficos/                  # onde os gráficos gerados são salvos
├── requirements.txt
└── README.md
```

## ▶️ Como rodar

1. Clone o repositório:
```bash
git clone https://github.com/SEU-USUARIO/previsao-vendas.git
cd previsao-vendas
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode o projeto:
```bash
python main.py
```

Os gráficos gerados serão salvos na pasta `graficos/`.

## 📝 Observação

Os dados usados neste exemplo são fictícios (gerados por `gerar_dados.py`).
Para usar dados reais, basta colocar um arquivo `vendas.csv` (com colunas
`ds` para data e `y` para valor de vendas) na pasta `dados/` e trocar a
chamada de `gerar_dados_exemplo()` por `pd.read_csv("dados/vendas.csv")`.
