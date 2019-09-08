import db_class
from db_credentials import oltp_db_config


def main():
    # call EXECUTER from oltp_load.py
    db = db_class.DbOps(**oltp_db_config)
    db.connection.commit() 


if __name__ == "__main__":
    main()
