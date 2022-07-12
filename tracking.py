from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config import PATH_OK, PATH_ERR
from file_manager import file_data_parse, file_manager
from models import add_new_flight
import shutil
from logger import get_logger

logger = get_logger(__name__)

class Handler(FileSystemEventHandler):
    """
    A class for tracking the creation of a new file
    """

    @staticmethod
    def move_file(path, flag):
        """
        Moving a file
        :param path: str
        :param flag: Boolean
        """
        logger.info('Старт функции перемещения файла')
        if flag:
            shutil.move(path, PATH_OK)
            logger.info('Файл перемещен в папку OK')
            return
        shutil.move(path, PATH_ERR)
        logger.info('Файл перемещен в папку ERR')

    def main(self, path):
        """
        Reads data from a file and serializes it to json format.
        Adds a new entry to the database.
        :param path: str
        """
        logger.info('Старт функции обработчика')
        flag = True
        try:
            file_name, date, flt, dep = file_data_parse(path)
            data = file_manager.read(path)
            file_manager.write(data)
        except Exception as e:
            logger.exception('Ошибка записи или чтения', e)
            flag = False
        try:
            add_new_flight(file_name, flt, date, dep)
            logger.info('Данные успешно загружены в БД!')
        except Exception as e:
            logger.exception('Ошибка загрузки данных в БД', e)
            flag = False
        try:
            self.move_file(path, flag)
            logger.info('Заввершение функции обработчика')
        except Exception as e:
            logger.exception('Ошибка при перемещении файла', e)

    def on_created(self, event):
        """
        Tracking the new appearance of new files
        :param event: object
        """
        logger.info(f'Обнаружен новый файл')
        file_name = file_data_parse(event.src_path)[0]
        logger.info(f'Имя файла:  {file_name}')
        self.main(event.src_path)

event_handler = Handler()
observer = Observer()
