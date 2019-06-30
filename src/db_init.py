from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True)
    department = Column(String(255), unique=True)


engine = create_engine('mysql+pymysql://pa_oltp:mypassword@127.0.0.1/pa_oltp')
Base.metadata.create_all(engine)