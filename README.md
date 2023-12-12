# 'PEP parsing project' created by Pavel.
```
https://github.com/pgphil86
```
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
### Languages:
### I. [Русский язык.]()
### II. [English language.]()
## I. Проект 'PEP парсинг'.

### Описание проекта.

Проект, созданный для парсинга документации Python. Выводы в терминал могут быть в строчном виде или в табличном. Есть сохранение результатов в файл .csv.

### Режимы работы парсера.
1. whats-new (получение ссылок с новыми версиями Python.)
1. latest-version (получение ссылок на каждую версию Python.)
1. download (скачивание архива документации для последней версии Python.)
1. pep (анализ статусов PEP документации.)
### Работа с проектом.
В первую очередь необходимо склонировать репозиторий.
```
git@github.com:pgphil86/bs4_parser_pep.git
```
Переходим в корневую директорию проекта.
```
cd  bs4_parser_pep/
```
Создаём и активируем виртуальное окружения для нашего проекта. А также обновляем службу pip.
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
```
Далее устанавливаем зависимости из файла requirements.txt.
```
pip install -r requirements.txt
```
В директории src/ можно ознакомиться с документацией.
```
cd src/
python3 main.py -h
```
Документация будет такого вида.
```
usage: main.py [-h] [-c] [-o {pretty,file}] {whats-new,latest-versions,download,pep}

Парсер документации Python

positional arguments:
  {whats-new,latest-versions,download,pep}
                        Режимы работы парсера

options:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}
                        Дополнительные способы вывода данных
```
Выбор режима работы парсера.
```
python3 main.py whats-new
```
```
python3 main.py latest-versions
```
```
python3 main.py download
```
```
python3 main.py pep
```
Для очистки кеша необходимо использовать -c или --clear-cache.
```
python3 main.py -c
```
## II. 'PEP parsing project'.

### Description of the project.
A project created for parsing Python documentation. The outputs to the terminal can be in lowercase or tabular form. There is a saving of the results to a .csv file.
### The modes of operation of the parser.
1. whats-new (getting links with new versions of Python.)
1. latest-version (getting links to each version of Python.)
1. download (downloading the documentation archive for the latest version of Python.)
1. pep (analyzing the status of PEP documentation.)
### Working with the project.
First of all, you need to clone the repository.
```
git@github.com:pgphil86/bs4_parser_pep.git
```
Go to the root directory of the project.
```
cd  bs4_parser_pep/
```
We create and activate a virtual environment for our project. We are also updating the pip service.
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
```
Next, install the dependencies from the file requirements.txt .
```
pip install -r requirements.txt
```
The documentation can be found in the src/ directory.
```
cd src/
python3 main.py -h
```
The documentation will be of this type.
```
usage: main.py [-h] [-c] [-o {pretty,file}] {whats-new,latest-versions,download,pep}

Парсер документации Python

positional arguments:
  {whats-new,latest-versions,download,pep}
                        Режимы работы парсера

options:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}
                        Дополнительные способы вывода данных
```
Selecting the parser's operating mode.
```
python3 main.py whats-new
```
```
python3 main.py latest-versions
```
```
python3 main.py download
```
```
python3 main.py pep
```
To clear the cache, use -c or --clear-cache.
```
python3 main.py -c
```
