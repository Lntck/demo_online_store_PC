import cgi
import sqlite3
import sys
import codecs



rating = ["4.7", "4.8", "4.9", "4.77", "4.89", "4.69"]
otz = ["9", "14", "13", "18", "7", "19"]
c = 0

connection = sqlite3.connect('katalog.db')
cursor = connection.cursor()
cursor.execute("Select * from products")
data = cursor.fetchall()
connection.commit()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
for i in data:
    c += 1
    print(f"""
            <li class="products-grid__item">
              <article class="product">
                <a href="#" class="product__image">
                  <div class="product__switch image-switch">
                    <div class="image-switch__item">
                      <div class="image-switch__img"><img src="{i[2].split(";")[0]}" alt="Макбук" id="img{c}"></div>
                    </div>
                    <div class="image-switch__item">
                      <div class="image-switch__img"><img src="{i[2].split(";")[1]}" alt="Макбук"></div>
                    </div>
                    <div class="image-switch__item">
                      <div class="image-switch__img"><img src="{i[2].split(";")[2]}" alt="Макбук"></div>
                    </div>
                  </div>
                  <ul class="product__image-pagination image-pagination" aria-hidden="true"></ul>
                </a>
                <h3 class="product__title">
                  <p href="#" id="name{c}">{i[1]}</p>
                </h3>
                <div class="product__props">
                  <span class="product__rating">
                    <svg width="16" height="15" viewBox="0 0 16 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path
                        d="M7.04894 0.92705C7.3483 0.00573924 8.6517 0.00573965 8.95106 0.92705L10.0206 4.21885C10.1545 4.63087 10.5385 4.90983 10.9717 4.90983H14.4329C15.4016 4.90983 15.8044 6.14945 15.0207 6.71885L12.2205 8.75329C11.87 9.00793 11.7234 9.4593 11.8572 9.87132L12.9268 13.1631C13.2261 14.0844 12.1717 14.8506 11.388 14.2812L8.58779 12.2467C8.2373 11.9921 7.7627 11.9921 7.41221 12.2467L4.61204 14.2812C3.82833 14.8506 2.77385 14.0844 3.0732 13.1631L4.14277 9.87132C4.27665 9.4593 4.12999 9.00793 3.7795 8.75329L0.979333 6.71885C0.195619 6.14945 0.598395 4.90983 1.56712 4.90983H5.02832C5.46154 4.90983 5.8455 4.63087 5.97937 4.21885L7.04894 0.92705Z" />
                    </svg>
                    {rating[c%6]}
                  </span>
                  <span class="product__testimonials">{otz[c%6]} отзывов</span>
                </div>
                <div class="product__info">
                  <span class="product__available">{i[3]}</span>
                </div>
                <div class="product__price product-price">
                  <span class="product-price__current" id="price{c}">{i[4]} ₽</span>
                  <span class="product-price__old">{int(i[4]) + 10500} ₽</span>
                </div>
                <button class="product__btn btn" onclick="cart(this)" id="{c}">Добавить в корзину</button>
              </article>
            </li>
    """)
    # print(f"""
    # <li class="products-grid__item">
    #     <article class="product">
    #                     <a href="#" class="product__image">
    #                     <div class="product__switch image-switch">
    #                         <div class="image-switch__item">
    #                         <div class="image-switch__img"><img src="https://avatars.mds.yandex.net/get-mpic/6237625/img_id3925425808395649083.jpeg/orig" alt="Макбук"></div>
    #                         </div>
    #                         <div class="image-switch__item">
    #                         <div class="image-switch__img"><img src="https://avatars.mds.yandex.net/get-mpic/6321906/img_id5617113514299403325.jpeg/orig" alt="Макбук"></div>
    #                         </div>
    #                         <div class="image-switch__item">
    #                         <div class="image-switch__img"><img src="https://avatars.mds.yandex.net/get-mpic/6647093/img_id2726864551170744350.jpeg/orig" alt="Макбук"></div>
    #                         </div>
    #                     </div>
    #                     <ul class="product__image-pagination image-pagination" aria-hidden="true"></ul>
    #                     </a>
    #                     <h3>
    #                     pc
    #                     </h3>
    #                     <div class="product__props">
    #                     <span class="product__rating">
    #                         <svg width="16" height="15" viewBox="0 0 16 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    #                         <path
    #                             d="M7.04894 0.92705C7.3483 0.00573924 8.6517 0.00573965 8.95106 0.92705L10.0206 4.21885C10.1545 4.63087 10.5385 4.90983 10.9717 4.90983H14.4329C15.4016 4.90983 15.8044 6.14945 15.0207 6.71885L12.2205 8.75329C11.87 9.00793 11.7234 9.4593 11.8572 9.87132L12.9268 13.1631C13.2261 14.0844 12.1717 14.8506 11.388 14.2812L8.58779 12.2467C8.2373 11.9921 7.7627 11.9921 7.41221 12.2467L4.61204 14.2812C3.82833 14.8506 2.77385 14.0844 3.0732 13.1631L4.14277 9.87132C4.27665 9.4593 4.12999 9.00793 3.7795 8.75329L0.979333 6.71885C0.195619 6.14945 0.598395 4.90983 1.56712 4.90983H5.02832C5.46154 4.90983 5.8455 4.63087 5.97937 4.21885L7.04894 0.92705Z" />
    #                         </svg>
    #                         7
    #                     </span>
    #                     <span class="product__testimonials">{otz[c%6]} отзывов</span>
    #                     </div>
    #                     <div class="product__info">
    #                     <span class="product__term">Артикул: 134134</span>
    #                     <span class="product__available">В наличии: 4 шт</span>
    #                     </div>
    #                     <div class="product__price product-price">
    #                     <h3 style="display: none;">dawsdwa</h3>
    #                     <p>
    #                         <span class="price">Price: $23.44</span>
    #                         <br>
    #                         <br>
    #                         <br>
    #                         <span class="add-to-cart-btn">Добавить в корзину</span>
    #                     </p>
    #     </article>
    # </li>""")

connection.close()