import pandas as pd
import numpy as np
import sklearn.datasets

def load_data():
    file_path = input("Введите путь к файлу CSV (или нажмите Enter для датасета diabetes): ")
    if file_path:
        table = pd.read_csv(file_path)
        print(f"Таблица загружена из {file_path}")
    else:
        diabetes = sklearn.datasets.load_diabetes()
        table = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
        print("Датасет diabetes загружен")
    return table

def create_feature(table, column_name):
    if column_name not in table.columns:
        print(f"Ошибка: Столбец '{column_name}' не найден. Доступные столбцы: {', '.join(list(table.columns))}")
        return table
    
    if not np.issubdtype(table[column_name].dtype, np.number):
        print(f"Ошибка: Столбец '{column_name}' не числовой (тип: {table[column_name].dtype})")
        return table
    
    condition = table[column_name] > table[column_name].mean()
    new_feature_name = f"{column_name}_above_mean"
    table[new_feature_name] = np.where(condition, 1, 0)
    print(f"Среднее значение {column_name}: {table[column_name].mean():.6f}")
    print("Первые 6 строк DataFrame с новым признаком:")
    print(table.head(6))
    print(f"Распределение нового признака '{new_feature_name}':")
    print(table[new_feature_name].value_counts())
  
    return table
  
table = load_data()
column = input("Доступные столбцы: " + ', '.join(list(table.columns)) + "\nВыберите столбец:")
table = create_feature(table, column)
