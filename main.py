import time
from config import PATH_IN
from tracking import observer, event_handler
from models import add_new_flight, Session, Flight, connection
from file_manager import file_data_parse, file_manager

def start_app():
    """
    Starts the file tracking program.
    """

    observer.schedule(event_handler, PATH_IN)
    observer.start()
    try:
        while True:
            time.sleep(90)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

# Написать SQL запрос для выборки из таблицы 'flight' всех рейсов за определённую дату
# def test_query(date):
#     with Session() as session:
#         res = session.query(Flight).filter(Flight.depdate == date).all()
#         print(res)
#     result = connection.execute(f"""SELECT * FROM flight WHERE flight.depdate = '2020-11-11';""").fetchall()
#     print(result)
#
# test_query('20201111')

if __name__ == '__main__':
    start_app()
