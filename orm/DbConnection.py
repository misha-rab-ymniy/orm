import psycopg2
import json


class Connection:
    _connection = None
    _cursor = None

    def __init__(self):
        with open('../orm/orm/db_config.json') as file:
            data = json.load(file)
        self._connection = psycopg2.connect(**data)
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

    def insert(self, table_name: str, attrs: tuple, data: tuple):
        str_attrs = f'{attrs}'.replace("'", '"')
        str_data = f'{data}'[1:-1]
        sql_request = f'''INSERT INTO "{table_name}"{str_attrs} VALUES {str_data}'''
        print(sql_request)
        self._cursor.execute(sql_request)
        self._connection.commit()

    def delete(self, table_name: str):
        raise NotImplementedError
