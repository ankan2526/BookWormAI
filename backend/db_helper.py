

class DB_Helper:
    def __init__(self):
        pass

    def get_books(self, conn):
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM books LIMIT 100;
        ''')
        result = cursor.fetchall()
        cursor.close()
        return list(result)
    