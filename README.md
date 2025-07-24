# Análise de Regressão Linear para Níveis de CO₂

Este projeto consiste em um script Python que calcula a reta de regressão linear para um conjunto de dados. Ele foi desenvolvido para resolver um problema específico de análise da variação do nível de CO₂ atmosférico ao longo dos anos, conforme descrito em "Cálculo, vol. 1, Stewart".

O objetivo é encontrar os coeficientes `m` (inclinação) e `b` (interceptação) da reta $y = mx + b$ que melhor se ajusta aos dados fornecidos. Estes coeficientes são determinados ao se encontrar os **pontos críticos** da função de soma dos quadrados dos erros, $g(m, b)$.

## Descrição do Problema

O programa recebe uma tabela de dados com os anos ($x_i$) e os respectivos níveis de CO₂ em ppm ($y_i$). A partir desses dados, ele deve:
1.  Calcular os coeficientes `m` e `b` da reta de regressão.
2.  Verificar se os valores encontrados correspondem aos valores de referência: $m = 1,65429$ e $b = -2938,07$.
3.  Visualizar os dados e a reta de regressão em um gráfico.

## Requisitos

Para executar o script, você precisará ter o Python 3 instalado, juntamente com as seguintes bibliotecas:

-   **NumPy:** Para cálculos numéricos eficientes.
-   **Matplotlib:** Para a visualização dos dados e da reta de regressão.

Você pode instalar estas bibliotecas usando o `pip`:

```bash
pip install numpy matplotlib