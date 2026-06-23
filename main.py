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