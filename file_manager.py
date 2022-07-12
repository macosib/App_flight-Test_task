import json
import csv
import os
from datetime import datetime
from config import PATH_OUT
from logger import get_logger

logger = get_logger(__name__)

def file_data_parse(path):
    """
    Parsing data from the file name
    """
    logger.info(f'Старт парсинга данных с {path}')
    result = []
    name = path.split('/In/')[1]
    data = name.strip('.csv').split('_')
    result.append(name)
    result.extend(data)
    logger.info(f'Завршение парсинга данных с {path}')
    return result

class FileActions:
    """
    A class for reading a csv file and writing to json format
    """

    @staticmethod
    def _date_format(date_str, date_format='%Y%m%d'):
        logger.info(f'Форматирование даты {date_str}')
        return datetime.strptime(date_str, date_format).date().isoformat()

    def read(self, path):
        """
        Reading data from a csv file
        :param path: str
        """
        logger.info(f'Начало чтения файла {path}')
        with open(path, encoding='utf-8') as file:
            data = []
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                row['bdate'] = self._date_format(row.get('bdate'), '%d%b%y')
                data.append(row)
        file_name, date, flt, dep = file_data_parse(path)
        result = {
            'flt': flt,
            'date': self._date_format(date),
            'dep': dep,
            'prl': data,
        }
        logger.info(f'Завершение чтения файла {file_name}')
        return result

    def write(self, data):
        """
        Writing data to a json file
        :param data: dict
        """
        logger.info('Начало записи файла!')
        file_name = f"{''.join(data.get('date').split('-'))}_{data.get('flt')}_{data.get('dep')}.json"
        path = os.path.join(PATH_OUT, file_name)
        with open(path, "w") as file:
            json.dump(data, file, indent=2)
        logger.info('Запись завершена!')
        return True

file_manager = FileActions()
