<h2 align="center">Blog FastAPI</h2>


### Описание проекта:
Блог написаный на FastAPI.
- JWT авторизация
- CRUD пользователей
- CRUD категорий
- CRUD статей
- Отправка Email

### Инструменты разработки

**Стек:**
- Python >= 3.7
- FastAPI == 0.52.0
- PostgreSQL

**Ссылки**:
- [Канал Youtube](https://www.youtube.com/channel/UC_hPYclmFCIENpMUHpPY8FQ?view_as=subscriber)
- [Telegram](https://t.me/trueDjangoChannel)
- [Группа в VK](https://vk.com/djangochannel)

## Разработка

##### 1) Сделать форк репозитория и поставить звездочку)

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) Создать виртуальное окружение

    python -m venv venv
    
##### 4) Активировать виртуальное окружение

##### 5) В папке `core` файл `local_config.py-example` переименовать в `local_config.py` и прописать конект к базе

##### 6) Устанавливить зависимости:

    pip install -r req.txt

##### 7) Выполнить команду для выполнения миграций

    alembic upgrade head
    
##### 8) Создать суперпользователя

    в разработке
    
##### 9) Запустить сервер

    uvicorn main:app --reload
    
##### 10) Перейти по адресу

    http://127.0.0.1:8000/docs
    
## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2020-present, DJWOMS - Omelchenko Michael



