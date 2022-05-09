import sqlite3

class Database():
    def __init__(self):
        self.stock_target_price = {}
    
    def get_stock_db(self):
        return self.stock_target_price
        
    def update(self):
        connection = sqlite3.connect('stock_target.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS stocks (name text, target real)')
        connection.commit()

        for row in cursor.execute('SELECT * FROM stocks'):
            stock_name = row[0]
            stock_target = row[1]
            self.stock_target_price[stock_name] = stock_target
        connection.close()
    
    def add_stock_name_target(self, name, target):
        connection = sqlite3.connect('stock_target.db')
        cursor = connection.cursor()
        params = [(f'{name}', f'{target}'),]
        cursor.executemany('INSERT INTO stocks VALUES (?,?)', params)
        connection.commit()
        connection.close()
        self.update()
        
    def remove_stock(self, name):
        connection = sqlite3.connect('stock_target.db')
        cursor = connection.cursor()
        print(name + ' removed')
        cursor.execute(f'''delete from stocks where name='{name}' ''')
        connection.commit()
        connection.close()
        self.update()
    
    def clear_database(self):
        connection = sqlite3.connect('stock_target.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM stocks')
        connection.commit()
        connection.close()
        self.update()