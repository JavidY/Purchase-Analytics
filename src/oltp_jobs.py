import config
from mappings import Mappings
from sql_queries import depts_load_sql, depts_query_sql
from db_credentials import oltp_db_config
from db_class import DbClass

# create mapping object for departments table. Source departments.csv target OLTP.departments
tgt_conn = DbClass(**oltp_db_config)
csv_conn = config.get_input_folder()
src_parameters = ("departments.csv", csv_conn, Mappings.types["csv"])
tgt_parameters = (depts_query_sql, tgt_conn, depts_load_sql, Mappings.types["rdbms"])
m_depts = Mappings(*src_parameters, *tgt_parameters)
jobs = [m_depts]
