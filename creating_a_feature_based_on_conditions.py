import pandas as pd
import os
from sklearn.datasets import load_diabetes

def load_data():
    """Загружает датасет из CSV файла или использует дефолтный, если пустой ввод
    Возвращает:
        pd.DataFrame: Загруженный датасет типа DataFrame.
    """
    while True:
        file_path = input("Введите путь к файлу CSV (или нажмите Enter для датасета diabetes): ")
        if not file_path:
            diabetes = load_diabetes()
            print("Датасет diabetes загружен")
            return pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
        if not os.path.isfile(file_path):
            print("Файл не найден, попробуйте ещё раз")
            continue
        if os.path.getsize(file_path) == 0:
            print("CSV файл пустой, попробуйте ещё раз")
            continue
        df = pd.read_csv(file_path)
        if df.empty:
            print("CSV файл не содержит данных, попробуйте ещё раз")
            continue
        print(f"Таблица загружена из {file_path}")
        return df

def create_feature(table, column_name):
    """Создать бинарный признак, указывающий, превышают ли значения в столбце среднее значение
    Аргументы:
        table (pd.DataFrame): входящая таблица.
        column_name (str): Имя колонки колонки для использования.

    Вернёт:
        кортеж: (DataFrame с новым признаком, имя признака).
    """
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
    """Главная функция
    Загружаем датасет через load_data выше, выбираем столбец"""
    table = load_data()
    print("Доступные столбцы:", list(table.columns))

    column = input("Выберите столбец: ")
    if column in table.columns:
        table, new_feature_name = create_feature(table, column)
        print(f"Новая фича '{new_feature_name}' создана")
    else:
        print(f"Ошибка: Столбец '{column}' не найден")

if __name__ == "__main__":
    main()