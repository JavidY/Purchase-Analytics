depts_load_sql = """INSERT INTO departments
                     (department_id, department) VALUES (%s, %s)"""


depts_query_sql = """SELECT department_id, department FROM departments"""
