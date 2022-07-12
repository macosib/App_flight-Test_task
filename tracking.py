from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config import PATH_OK, PATH_ERR
from file_manager import file_data_parse, file_manager
from models import add_new_flight
import shutil

class Handler(FileSystemEventHandler):
    """
    A class for tracking the creation of a new file
    """

    @staticmethod
    def move_file(path, flag):
        print(path)
        if flag:
            shutil.move(path, PATH_OK)
            print(f'Файл перемещен в папку OK')
            print()
            return
        shutil.move(path, PATH_ERR)
        print(f'Файл перемещен в папку ERR')
        print()

    def main(self, path):
        flag = True
        try:
            file_name, date, flt, dep = file_data_parse(path)
            data = file_manager.read(path)
            file_manager.write(data)
        except Exception:
            print(f'Ошибка записи или чтения')
            flag = False
        try:
            add_new_flight(file_name, flt, date, dep)
            print(f'Данные успешно загружены в БД!')
        except Exception:
            print(f'ошибка загрузки данных в БД')
            flag = False
        try:
            self.move_file(path, flag)
        except:
            print(f'Ошибка при перемещении файла')

    def on_created(self, event):
        """
        Reads data from a file and serializes it to json format.
        Adds a new entry to the database.
        :param event: object
        """
        file_name = file_data_parse(event.src_path)[0]
        print(f'Обнаружен новый файл:  {file_name}')
        self.main(event.src_path)

event_handler = Handler()
observer = Observer()
