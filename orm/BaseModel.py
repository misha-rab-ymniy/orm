from .DbConnection import Connection as Conn

_connection = Conn()


class BaseModel:
    _name: str

    def __init__(self):
        self._name = type(self).__name__

    def select(self, columns: tuple = None):
        if columns is None:
            data = _connection.select(self._name)
            obj_data = []
            for obj in data:
                use = locals()['self'].__class__()
                attributes = use.__class__.__dict__['__annotations__']
                i = 0
                for attr in attributes.keys():
                    use.__dict__[attr] = obj[i]
                    i += 1
                obj_data.append(use)
            return obj_data
        else:
            data = _connection.select(self._name, columns)
            return data

    def update(self, data: dict, condition: str = None):
        _connection.update(self._name, data, condition)

    def insert(self, *values: tuple):
        attrs = tuple([type(self).__dict__['__annotations__'].keys()][0])[1:]
        _connection.insert(self._name, attrs, values)

    def delete(self, condition: str = None):
        _connection.delete(self._name, condition)

    @staticmethod
    def execute(sql_request: str):
        _connection.execute(sql_request)

    def __str__(self):
        attributes = type(self).__dict__['__annotations__']
        string = f"{type(self).__name__}("
        for attr in attributes.keys():
            string += f"{attr} : {self.__dict__[attr]}, "
        string += ')'
        return string
