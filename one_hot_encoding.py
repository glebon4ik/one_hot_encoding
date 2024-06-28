import pandas as pd
import random

# Создание исходного DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Original DataFrame:")
print(data.head())

# Преобразование в one hot вид вручную
one_hot_df = pd.DataFrame()

# Получение уникальных значений
unique_values = data['whoAmI'].unique()

# Создание one hot столбцов
for value in unique_values:
    one_hot_df[value] = (data['whoAmI'] == value).astype(int)

print("\nOne Hot Encoded DataFrame:")
print(one_hot_df.head())

# Вывод окончательного DataFrame
one_hot_data = pd.concat([data, one_hot_df], axis=1)
print("\nFinal DataFrame with One Hot Encoding:")
print(one_hot_data.head())
