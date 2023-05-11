import json
import cgi
import sqlite3
import sys
import codecs

info_browser = cgi.FieldStorage()
list_shop = json.loads(info_browser.getfirst("list_cart", None))

connection = sqlite3.connect('katalog.db')
cursor = connection.cursor()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

d = {}
for i in list_shop:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for i in d.keys():
    cursor.execute(f"Select name, img_url, price from products where id = {str(i)}")
    data = cursor.fetchall()[0]
    print(f"""
                <div class="cart-wrapper">
                    <div class="cart-item">
                        <img src="{data[1].split(';')[0]}"> 
                        <div class="details">
                            <h4>{data[0]}</h4>
                            <span class="quantity">Кол-во:{d[i]}</span>
                            <span class="price">Цена:{data[2] * d[i]}₽</span>
                        </div>
                     </div>
        """)
connection.commit()