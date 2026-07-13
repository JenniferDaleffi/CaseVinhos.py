Separando variáveis explicativas e variável alvo
Removemos:
quality -> variável original usada para criar quality_binary
quality_binary -> variável alvo, não pode ficar dentro de X
Id -> identificador da linha, sem valor preditivo
X = df_pre.drop(columns=['quality', 'quality_binary', 'Id'])
y = df_pre['quality_binary']

print("Formato das variáveis explicativas X:", X.shape)
print("Formato da variável alvo y:", y.shape)