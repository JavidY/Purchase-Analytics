import os


# get OLTP db creds
DB_NAME_OLTP = os.environ.get("DB_NAME_OLTP")
DB_USER_OLTP = os.environ.get("DB_USER_OLTP")
DB_PASS_OLTP = os.environ.get("DB_PASS_OLTP")

# db config
oltp_db_config = {'user': DB_USER_OLTP, 'password': DB_PASS_OLTP, 'host': 'pa_db', 'database': DB_NAME_OLTP}
