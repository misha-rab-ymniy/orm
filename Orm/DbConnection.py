import psycopg2
import json


class Connection:
    _connection = None
    _cursor = None

    def __init__(self):
        with open('./Orm/db_config.json') as file:
            data = json.load(file)
        self._connection = psycopg2.connect(**data)
        self._cursor = self._connection.cursor()

    def select(self, table_name: str, columns: tuple = None, condition: str = None) -> tuple:
        if condition is None:
            condition_str = ""
        else:
            condition_str = f" WHERE {condition}"
        if columns is None:
            columns_str = "*"
        else:
            columns_str = ", ".join(columns)
        sql_request = f'''SELECT {columns_str} FROM "{table_name}"{condition_str}'''
        self._cursor.execute(sql_request)
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
        if len(data) == 1:
            str_data = f'{data}'[1:-2]
        else:
            str_data = f'{data}'[1:-1]
        sql_request = f'''INSERT INTO "{table_name}"{str_attrs} VALUES {str_data}'''
        try:
            self._cursor.execute(sql_request)
            self._cursor.execute('SELECT LASTVAL()')
            self._connection.commit()
        except Exception as e:
            self._cursor.execute("ROLLBACK")
            raise e

    def delete(self, table_name: str, condition: str = None):
        condition = ' WHERE ' + condition if condition else ''
        sql_request = f'''DELETE FROM "{table_name}"{condition}'''
        self._cursor.execute(sql_request)
        self._connection.commit()

    def execute(self, sql_request: str):
        self._cursor.execute(sql_request)
        self._connection.commit()
        return self._cursor.fetchall()
