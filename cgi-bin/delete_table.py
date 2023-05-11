import cgi
from db_utils import exec_sql

exec_sql(f"delete from products where id={cgi.FieldStorage().getvalue('id')}")