from sqlalchemy import inspect, create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('mysql+pymysql://pa_oltp:mypassword@127.0.0.1/pa_oltp')


class Department(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True)
    department = Column(String(255), unique=True)


def create_tables():
    Base.metadata.create_all(engine)


def db_init_tables():
    return inspect(engine).get_table_names()


# Create empty database tables
create_tables()
print(db_init_tables())
