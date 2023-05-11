import cgi
from db_utils import exec_sql

exec_sql(f"insert into products(name, img_url, description, price) values('{cgi.FieldStorage().getvalue('name')}', '{cgi.FieldStorage().getvalue('img')}', '{cgi.FieldStorage().getvalue('description')}', '{cgi.FieldStorage().getvalue('price')}');")