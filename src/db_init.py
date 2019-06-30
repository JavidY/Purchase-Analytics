from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://pa_oltp:mypassword@127.0.0.1/pa_oltp')
engine.connect()