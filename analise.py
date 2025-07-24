import numpy as np
import matplotlib.pyplot as plt

def calcular_regressao_linear(x, y):
    x_array = np.array(x)
    y_array = np.array(y)
    
    n = len(x_array)
    
    soma_x = np.sum(x_array)
    soma_y = np.sum(y_array)
    soma_xy = np.sum(x_array * y_array)
    soma_x_quadrado = np.sum(x_array**2)
    
    
    numerador_m = n * soma_xy - soma_x * soma_y
    denominador_m = n * soma_x_quadrado - soma_x**2
    m = numerador_m / denominador_m
    
    b = (soma_y - m * soma_x) / n
    
    return m, b

anos = [1980, 1982, 1984, 1986, 1988, 1990, 1992, 1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008]
niveis_co2 = [338.7, 341.2, 344.4, 347.2, 351.5, 354.2, 356.3, 358.6, 362.4, 366.5, 369.4, 373.2, 377.5, 381.9, 385.6]

m_calculado, b_calculado = calcular_regressao_linear(anos, niveis_co2)

print("Análise de Regressão Linear para Níveis de CO₂\n")
print(f"Os pontos críticos da função g(m, b), que fornecem os coeficientes da reta de regressão, são:")
print(f"m (inclinação) = {m_calculado}")
print(f"b (interceptação) = {b_calculado}\n")

print("A equação da reta de regressão é: CO₂_level = {:.5f} * Year + {:.2f}\n".format(m_calculado, b_calculado))

m_esperado = 1.65429
b_esperado = -2938.07
print("Verificação dos Resultados")
print(f"Valor de 'm' esperado: {m_esperado}")
print(f"Valor de 'm' calculado: {m_calculado:.5f}")
print(f"\nValor de 'b' esperado: {b_esperado}")
print(f"Valor de 'b' calculado: {b_calculado:.2f}")

plt.figure(figsize=(10, 6))
plt.scatter(anos, niveis_co2, color='blue', label='Dados Originais')
plt.plot(anos, m_calculado * np.array(anos) + b_calculado, color='red', label='Reta de Regressão')
plt.title('Nível de CO₂ vs. Ano')
plt.xlabel('Ano')
plt.ylabel('Nível de CO₂ (ppm)')
plt.legend()
plt.grid(True)
plt.show()