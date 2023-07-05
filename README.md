# Python парсер PEP

## Парсинг документации PEP
> Парсер получает информацию обо всех PEP документах

## Стек технологий:
- Python
- BeautifulSoup4
- Logging
- Prettytable

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/vartexxx/bs4_parser_pep.git

cd bs4_parser_pep
```

Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv venv

. venv/bin/activate
```

Обновить пакетный менеджер и установить зависимости:
```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

## Список поддерживаемых комманд:
Вывод справки:
```
python main.py pep -h
```

Создание csv файла с таблицей:
```
python main.py pep -o file
```

Вывод таблицы prettytable:
```
python main.py latest-versions -o pretty 
```

Вывод ссылок нововведений в python:
```
python main.py whats-new
```
