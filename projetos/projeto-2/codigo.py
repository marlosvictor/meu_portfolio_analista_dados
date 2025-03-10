import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Carregar os dados
try:
    dados = pd.read_csv(r'C:\Users\Cliente\Desktop\meu-portfolio-analista-dados\projetos\projeto-2\notas.csv')
    print("Dados carregados com sucesso!")
except FileNotFoundError:
    print("Erro: Arquivo 'notas.csv' não encontrado. Verifique o caminho do arquivo.")
    exit()


# Mostrar as primeiras linhas dos dados
print("\nDados de Notas:")
print(dados.head())

# Heatmap de correlação
print("\nCorrelação entre as variáveis:")
correlacao = dados.select_dtypes(include=['number']).corr()
print(correlacao)

plt.figure(figsize=(8, 6))
sns.heatmap(correlacao, annot=True, cmap='coolwarm')
plt.title('Correlação entre Variáveis')
plt.show()

# Regressão Linear: Prever Notas de Português com base em Matemática
X = dados[['Nota_Matematica']]  # Variável independente
y = dados['Nota_Portugues']     # Variável dependente

# Criar e treinar o modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Adicionar as previsões ao DataFrame
dados['Previsao_Portugues'] = modelo.predict(X)

# Gráfico de dispersão com linha de regressão
plt.figure(figsize=(10, 6))
plt.scatter(dados['Nota_Matematica'], dados['Nota_Portugues'], color='blue', label='Dados Reais')
plt.plot(dados['Nota_Matematica'], dados['Previsao_Portugues'], color='red', label='Linha de Regressão')
plt.title('Relação entre Notas de Matemática e Português')
plt.xlabel('Notas de Matemática')
plt.ylabel('Notas de Português')
plt.legend()
plt.show()

# Exibir coeficientes da regressão
print(f"\nCoeficiente da regressão: {modelo.coef_[0]}")
print(f"Intercepto: {modelo.intercept_}")