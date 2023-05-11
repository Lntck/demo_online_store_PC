import cgi
import sqlite3
import sys
import codecs


connection = sqlite3.connect('katalog.db')
cursor = connection.cursor()
cursor.execute("Select * from products")
data = cursor.fetchall()
connection.commit()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
for i in data:
    print(f"""
            <tr>
                <td>{i[0]}</td>
                <td>{i[1]}</td>
                <td>{i[2]}</td>
                <td>{i[3]}</td>
                <td>{i[4]}</td>
            </tr>
    """)

connection.close()