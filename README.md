# creating-a-feature-based-on-conditions
Этот скрипт на Python обрабатывает табличные данные, создавая новый бинарный признак на основе выбранного числового столбца. Пользователь может загрузить свою таблицу из CSV-файла или использовать встроенный датасет diabetes из библиотеки scikit-learn. Скрипт проверяет, является ли выбранный столбец числовым, и создаёт новый столбец <column_name>_above_mean, где:  
  1 - если значение в выбранном столбце больше среднего по этому столбцу.  
  0 - в ином случае.  

## Установка

1. **Клонируйте репозиторий** (Если применимо):
   ```bash
   git clone <repository-url>
   cd p1_feature_based_on_conditions/creating-a-feature-based-on-conditions
   ```

2. **Создайте и активируйте виртуальную среду (venv)**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # На Windows используйте Git Bash или Powershell
   ```

3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

## Использование

1. **Запуск скрипта**:
   ```bash
   python creating_a_feature_based_on_conditions.py
   ```

2. **Следуйте инструкциям, которые будут выведены**:
   - Введите путь к файлу CSV или нажмите Enter, чтобы использовать датасет `diabetes`.  
   - Введите имя столбца для создания признака (например, bmi для датасета diabetes).

## Пример

```bash
$ python creating_a_feature_based_on_conditions.py
Введите путь к файлу CSV (или нажмите Enter для датасета diabetes): 
Датасет diabetes загружен
Доступные столбцы: ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
Выберите столбец: bmi
Новый признак 'bmi_above_mean' создан
```