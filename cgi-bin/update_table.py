import cgi
from db_utils import exec_sql


exec_sql(f"update products set name='{cgi.FieldStorage().getvalue('name')}', description='{cgi.FieldStorage().getvalue('description')}', price={cgi.FieldStorage().getvalue('price')} where id={cgi.FieldStorage().getvalue('id')}")