### *   *   *   Бот Compas  *   *   *

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/PetrovichOriginal/compas_bot.git
```

```
cd compas_bot
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
. venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустить проект:

```
python compasbot.py
```

Данные для бота:

```
Файлы для отправки хранятся в папке /root/data/
Имена и полные пути к файлам доступны в файле /root/data/'имена файлов.xlsx'
```