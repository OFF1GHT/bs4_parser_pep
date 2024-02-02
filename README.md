# Проект парсинга PEP

Этот проект представляет собой инструмент для парсинга данных о Python Enhancement Proposals (PEP). PEP - это документы, описывающие нововведения, улучшения или изменения в Python.

## Установка

### Клонируйте репозиторий:
```
git clone https://github.com/OFF1GHT/bs4_parser_pep.git
```

### Перейдите в директорию проекта:
```
cd bs4_parser_pep
```

### Создайте и активируйте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate
```

### Обновите pip:
```
pip install --upgrade pip
```

### Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

## Использование

### Просмотр режимов работы:
```
python src/main.py -h
```

### Вывод результатов в виде таблицы в терминале:
```
python src/main.py whats-new -o pretty
python src/main.py latest-versions -o pretty
python src/main.py pep -o pretty
```

### Сохранение результатов в файл:
```
python src/main.py latest-versions -o file
python src/main.py download
```

### Очистить кеш:
```
python src/main.py latest-versions -c -o pretty
python src/main.py download -c -o pretty
```
