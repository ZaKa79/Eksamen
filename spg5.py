import sqlite3
conn = sqlite3.connect('test_database.db')
c = conn.cursor()
try:
    c.execute('''
    CREATE TABLE IF NOT EXISTS products
    ([product_id] INTEGER PRIMARY KEY,
    [product_name] TEXT, [price] INTEGER)
    ''')
    c.execute('''
        INSERT INTO products (product_id, product_name, 
        price)
                VALUES
                (1,'Computer', 800),
                (2,'Printer', 200),
                (3,'Tablet', 300),
                (4,'Desk', 450),
                (5,'Chair', 150)
        ''')
    conn.commit()

    c.execute('''
            SELECT * FROM products WHERE price < 400;
            ''')
    rset = c.fetchall()
    print(f'Row-count : { len(rset) } ')
    for row in rset:
        print(f'name={row[1]} price={row[2]} \n')
except sqlite3.Error as e:
    print(f'Error calling SQL: "{e}"')
finally:
    conn.close()