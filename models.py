import sqlalchemy as sql
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from config import DB_USER, DB_NAME, DB_HOST, DB_PORT, DB_PASSWORD

Base = declarative_base()
engine = sql.create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()

class Flight(Base):
    """
    Class Flight creates a table "flight" in database "flight"
    """
    __tablename__ = "flight"
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True, nullable=False)
    file_name = sql.Column(sql.Text, nullable=False)
    flt = sql.Column(sql.Integer, nullable=False)
    depdate = sql.Column(sql.Date, nullable=False)
    dep = sql.Column(sql.Text, nullable=False)

    def __repr__(self):
        return f'{self.id} {self.flt} {self.depdate} {self.dep}'

def add_new_flight(file_name, flt, depdate, dep):
    """
    Adds new flight to database 'flight'
    :param file_name: str
    :param flt: int
    :param depdate: str
    :param dep: str

    :return: Boolean
    """
    new_flight = Flight(
        file_name=file_name,
        flt=flt,
        depdate=depdate,
        dep=dep,
    )
    session.add(new_flight)
    session.commit()
    return True

if __name__ == '__main__':
    Base.metadata.create_all(engine)