import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (15, 5)

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

# ВИЗУАЛИЗАЦИЯ ДАННЫХ

# -------------- Линейный график
plt.plot(random_nums_series, color="green")

# Подписи в таблице
plt.title("Линейный График Случайных Значений Массива")
plt.ylabel("Значение")
plt.xlabel("Порядковый индекс элемента")

plt.show()

# ------------- Гистограмма
rounded_nums_series = (random_nums_series / 100).round().astype(int) * 100
plt.hist(rounded_nums_series, bins=100, color="green")

# Шаг значений по оси x
x_ticks = np.arange(-10000, 10001, 1000)
plt.xticks(x_ticks, rotation=45)

# Подписи в таблице
plt.title("Гистограмма Случайных Чисел Массива округленных до 100")
plt.xlabel("Диапазон значений")
plt.ylabel("Частота")
plt.show()