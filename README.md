# SimpleAnalysis

Проект по анализу датасета, вывода базовых характеристик случайно сгенерированной подборки, визулизация данных при помощи 3 графиков и сохранение данных в файлы dataset.csv и отчет_по_статистике.txt

## Cтек

* **Язык программирования:** Python
* **Среда разработки:** PyCharm
* **Библиотеки:**
  * numpy 
  * pandas
  * matplotlib 
---

## Как клонировать и запустить

Для развертывания проекта локально выполните следующие шаги:

1. Клонирование репозитория
> Откройте терминал и склонируйте репозиторий:

```bash
git clone https://github.com/AleksandraTrunova/SimpleAnalysis.git
```
2. Перейдите в директорию проекта:
```bash
cd SimpleAnalysis
```

3. Установите виртуальное окружение и зависимости
```bash
python -m venv venv
.\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Запуск виртуального окружения и программы:
```bash
.\.venv\Scripts\activate.bat
python ./main.py
```