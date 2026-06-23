import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------- ПОЛУЧЕНИЕ НАБОРА ДАНЫЫХ
# Массив случайных чисел
random_nums_array = np.random.randint(-10000,10001, 1000)
# Объект Series
random_nums_series = pd.Series(random_nums_array)
random_nums_series.name = "Случайные_Числа"

# Вывод датасета в консоль
print(random_nums_series)
# Сохранение датасета в файл .csv
random_nums_series.to_csv("dataset.csv", index=False, header=False)

# Min/Max/Sum значения
min_val = random_nums_series.min()
max_val = random_nums_series.max()
sum_vals = random_nums_series.sum()

# Рассчеты Среднеквадратического отклонения и количества дубликатов
std_deviation = random_nums_series.std(ddof=0)
series_duplicates_count = random_nums_series.duplicated().sum()

# Вывод в консоль
print(f"Минимальное значение выборки: {min_val}")
print(f"Количество повторяющихся значений: {series_duplicates_count}")
print(f"Максимальное значение из набора данных: {max_val}")
print(f"Сумма чисел набора данных: {sum_vals}")
print(f"Среднеквадратическое отклонение набора данных: {std_deviation}")

# Запись отчета по статистике в файл
with open("отчет_по_статистике.txt", "w", encoding="utf-8") as file:
    file.write(f"Минимальное значение выборки: {min_val}\n")
    file.write(f"Количество повторяющихся значений: {series_duplicates_count}\n")
    file.write(f"Максимальное значение из набора данных: {max_val}\n")
    file.write(f"Сумма чисел набора данных: {sum_vals}\n")
    file.write(f"Среднеквадратическое отклонение набора данных: {std_deviation}\n")