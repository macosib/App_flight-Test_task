import json
import csv
import os
from datetime import datetime
from config import PATH_OUT


def file_data_parse(path):
    """
    Class Flight creates a table "flight" in database "flight"
    """
    result = []
    name = path.split('/In/')[1]
    data = name.strip('.csv').split('_')
    result.append(name)
    result.extend(data)
    return result

class FileActions:

    @staticmethod
    def _date_format(date_str, date_format='%Y%m%d'):
        return datetime.strptime(date_str, date_format).date().isoformat()

    def read(self, path):
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
        print(f'Файл {file_name} успешно прочитан!')
        return result

    def write(self, data):
        file_name = f"{''.join(data.get('date').split('-'))}_{data.get('flt')}_{data.get('dep')}.json"
        path = os.path.join(PATH_OUT, file_name)
        with open(path, "w") as file:
            json.dump(data, file, indent=2)

        print(f'Файл {file_name} успешно создан!')
        return True

file_manager = FileActions()
