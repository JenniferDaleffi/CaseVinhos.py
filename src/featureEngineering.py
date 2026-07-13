from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

Cópia da base original
df_pre = df.copy()

Garantia de que a variável alvo binária existe
if 'quality_binary' not in df_pre.columns:
    df_pre['quality_binary'] = np.where(df_pre['quality'] >= 7, 1, 0)

Feature Engineering
df_pre['total_acidity'] = (
    df_pre['fixed acidity'] +
    df_pre['volatile acidity'] +
    df_pre['citric acid']
)

df_pre['free_sulfur_ratio'] = (
    df_pre['free sulfur dioxide'] / (df_pre['total sulfur dioxide'] + 1e-6)
)

df_pre['sugar_alcohol_ratio'] = (
    df_pre['residual sugar'] / (df_pre['alcohol'] + 1e-6)
)

df_pre['alcohol_sulphates'] = (
    df_pre['alcohol'] * df_pre['sulphates']
)

print("Novas features criadas:")
print([
    'total_acidity',
    'free_sulfur_ratio',
    'sugar_alcohol_ratio',
    'alcohol_sulphates'
])

display(df_pre.head())