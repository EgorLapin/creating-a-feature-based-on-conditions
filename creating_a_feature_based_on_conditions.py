import pandas as pd
import os
from sklearn.datasets import load_diabetes

def load_data(file_path=None):
    """Загружает датасет из CSV файла или использует дефолтный, если путь не указан
    
    Аргументы:
        file_path (str, optional): Путь к CSV файлу. Если None, то загружается датасет diabetes.
    
    Возвращает:
        pd.DataFrame: Загруженный датасет типа DataFrame
    
    Вызывает:
        FileNotFoundError: Если файл не найден.
        ValueError: Если файл пустой или не содержит данных.
    """
    if not file_path:
        diabetes = load_diabetes()
        print("Датасет diabetes загружен")
        return pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")
    if os.path.getsize(file_path) == 0:
        raise ValueError(f"CSV файл {file_path} пустой")
    
    df = pd.read_csv(file_path)
    if df.empty:
        raise ValueError(f"CSV файл {file_path} не содержит данных")
    
    print(f"Таблица загружена из {file_path}")
    return df

def create_feature(table, column_name):
    """Создать бинарный признак, указывающий, превышают ли значения в столбце среднее значение.
    
    Аргументы:
        table (pd.DataFrame): Входящая таблица
        column_name (str): Имя столбца для обработки
    
    Возвращает:
        tuple: (DataFrame с новым признаком, имя нового признака)
    
    Вызывает:
        TypeError: Если table не является pd.DataFrame или column_name не строка
        KeyError: Если column_name отсутствует в table
        ValueError: Если столбец не содержит числовых данных
    """
    if not isinstance(table, pd.DataFrame):
        raise TypeError("Аргумент table должен быть pd.DataFrame")
    if not isinstance(column_name, str):
        raise TypeError("Аргумент column_name должен быть строкой")
    if column_name not in table.columns:
        raise KeyError(f"Столбец '{column_name}' не найден в таблице")
    if not pd.api.types.is_numeric_dtype(table[column_name]):
        raise ValueError(f"Столбец '{column_name}' должен содержать числовые данные")
    
    mean_value = table[column_name].mean()
    base_name = f"{column_name}_above_mean"
    new_feature_name = base_name
    index = 1
    while new_feature_name in table.columns:
        new_feature_name = f"{base_name}_{index}"
        index += 1
    table[new_feature_name] = (table[column_name] > mean_value).astype(int)
    return table, new_feature_name

def main():
    """Главная функция для взаимодействия с пользователем"""
    file_path = input("Введите путь к файлу CSV (или нажмите Enter для датасета diabetes): ")
    table = load_data(file_path)
    print("Доступные столбцы:", list(table.columns))
    
    column = input("Выберите столбец: ")
    if not isinstance(column, str) or column not in table.columns or not pd.api.types.is_numeric_dtype(table[column]):
        print(f"Ошибка: Столбец '{column}' некорректен или нечисловой")
        return
    table, new_feature_name = create_feature(table, column)
    print(f"Новая фича '{new_feature_name}' создана")
    print(table.head())

if __name__ == "__main__":
    main()