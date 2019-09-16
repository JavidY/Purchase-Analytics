# Insert statement for OLTP.departments table
depts_load_sql = """INSERT INTO OLTP.departments
                     (department_id, department) VALUES (%s, %s)"""

# Select statement for OLTP.departments table
depts_query_sql = """SELECT department_id, department FROM OLTP.departments"""
