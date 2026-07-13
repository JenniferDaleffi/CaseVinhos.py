Padronização das variáveis numéricas
scaler = StandardScaler()

Ajusta o scaler apenas nos dados de treino
X_train_scaled = scaler.fit_transform(X_train)

Aplica a mesma transformação nos dados de teste
X_test_scaled = scaler.transform(X_test)

Convertendo novamente para DataFrame
X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=X_train.columns,
    index=X_train.index
)

X_test_scaled = pd.DataFrame(
    X_test_scaled,
    columns=X_test.columns,
    index=X_test.index
)

print("Padronização concluída.")
display(X_train_scaled.describe().T[['mean', 'std']])