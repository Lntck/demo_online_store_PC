def exec_sql(sql_request):
    import sqlite3
    connection = sqlite3.connect('katalog.db')
    cursor = connection.cursor()
    cursor.execute(sql_request)
    connection.commit()
    connection.close()