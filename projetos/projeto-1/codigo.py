import pandas as pd
import matplotlib.pyplot as plt

meses_para_numero = {
    'Janeiro': 1,
    'Fevereiro': 2,
    'Março': 3,
    'Abril': 4,
    'Maio': 5,
    'Junho': 6,
    'Julho': 7,
    'Agosto': 8,
    'Setembro': 9,
    'Outubro': 10,
    'Novembro': 11,
    'Dezembro': 12
}

try:
    dados = pd.read_csv(r'C:\Users\Cliente\Desktop\meu-portfolio-analista-dados\projetos\projeto-1\vendas.csv')
    print("Dados carregados com sucesso!")
except FileNotFoundError:
    print("Erro: Arquivo 'vendas.csv' não encontrado. Verifique o caminho do arquivo.")
    exit()

dados['Mês'] = dados['Mês'].map(meses_para_numero)

print("\nDados de Vendas:")
print(dados.head())

total_vendas = dados.groupby('Produto')['Vendas'].sum()

print("\nTotal de Vendas por Produto:")
print(total_vendas)

total_vendas.plot(kind='bar', color='skyblue')
plt.title('Total de Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Vendas')
plt.show()