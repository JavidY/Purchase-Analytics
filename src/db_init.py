from sqlalchemy import create_engine, Table, MetaData, Column, String, Integer


engine = create_engine('mysql+pymysql://pa_oltp:mypassword@127.0.0.1/pa_oltp')
metadata = MetaData()


# tables
department = Table('departments', metadata,
                   Column('department_id', Integer(), primary_key=True),
                   Column('department', String(50)))


# Create database tables
metadata.create_all(engine)
