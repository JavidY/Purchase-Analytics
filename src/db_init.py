from sqlalchemy import create_engine, Table, MetaData, Column, String, Integer
import config


# build connection string for OLTP db
conn_str = 'mysql+pymysql://{0}:{1}@127.0.0.1/{2}'.format(config.DB_USER_OLTP,
                                                          config.DB_PASS_OLTP,
                                                          config.DB_NAME_OLTP)
engine = create_engine(conn_str)
metadata = MetaData()


# tables
department = Table('departments', metadata,
                   Column('department_id', Integer(), primary_key=True),
                   Column('department', String(50)))


if __name__ == '__main__':
    # Create database tables
    metadata.create_all(engine)
