import psycopg2


class Connection:
    _connection = None
    _cursor = None

    def __init__(self):
        self._connection = psycopg2.connect(database="cinema", host="localhost", user="mikhail", password="8057070Vb",
                                            port=5432)
        self._cursor = self._connection.cursor()

    def select(self, table_name: str) -> tuple:
        self._cursor.execute(f'''SELECT * FROM "{table_name}"''')
        data = self._cursor.fetchall()
        return data

    def update(self, table_name: str, data: dict, condition: str = None):
        str_data = ""
        count = len(data)
        i = 0
        for key, value in data.items():
            str_data += f"{key} = '{value}'"
            if i != count - 1:
                str_data += ', '
            i += 1
        condition = ' WHERE ' + condition if condition else ''
        sql_request = f'''UPDATE "{table_name}" SET {str_data}{condition}'''
        self._cursor.execute(sql_request)
        self._connection.commit()




