import sqlite3

# Создаем (или подключаемся к существующей) базу данных
conn = sqlite3.connect('sulpak.db')
cursor = conn.cursor()

# Создаем таблицу для хранения товаров
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        price REAL NOT NULL,
        link TEXT NOT NULL
    )
''')

# Вставляем данные о товарах в базу данных
cursor.executemany('''
    INSERT INTO products (name, description, price, link)
    VALUES (?, ?, ?, ?)
''', [
    ('Пылесос Xiaomi', 'Компактный и мощный пылесос с низким уровнем шума.', 85000, 'https://www.sulpak.kz/f/pylesosy_xiaomi'),
    ('Пылесос LG', 'Эффективный пылесос с технологией многослойной фильтрации.', 95000, 'https://www.sulpak.kz/f/pylesosy_lg'),
    ('Пылесос Philips', 'Мощный пылесос с высокой производительностью и фильтрацией воздуха.', 105000, 'https://www.sulpak.kz/f/pylesosy_philips'),
    ('Пылесос Samsung', 'Мощный пылесос с ярким дисплеем и отличной камерой.', 120000, 'https://www.sulpak.kz/f/pylesosy_samsung')
])

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных создана и данные добавлены!")