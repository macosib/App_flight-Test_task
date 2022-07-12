import os
from pathlib import Path

BASE_DIR = os.getcwd()
DB_USER = 'YOURLOGIN'  # Указать пользователя
DB_PASSWORD = 'YOURPASSWORD'  # Указать пароль
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'flight'

# Указать абсолютный путь до директории, например:
PATH_IN = f'{Path.home()}/In'
PATH_OUT = f'{Path.home()}/Out/'
PATH_OK = f'{Path.home()}/Ok/'
PATH_ERR = f'{Path.home()}/Err/'
# Если папки нужно создать в приложении, то можно указать так:
# PATH_IN = f'{BASE_DIR}/In'
# PATH_OUT = f'{BASE_DIR}/Out/'
