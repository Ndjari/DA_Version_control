
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=data)
plt.title('Preço da Gasolina em São Paulo (10 primeiros dias de Julho de 2021)')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

plt.savefig('gasolina.png')
