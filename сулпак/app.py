from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder='templates')  # Убедимся, что путь верный

# Функция для получения товаров из базы данных
def get_products():
    conn = sqlite3.connect('sulpak.db')
    cursor = conn.cursor()
    
    # Проверяем, существует ли таблица "products"
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
    if not cursor.fetchone():
        print("Ошибка: Таблица 'products' не найдена в базе данных.")
        return []  # Возвращаем пустой список, чтобы не было ошибки

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
