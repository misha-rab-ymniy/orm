from .DbConnection import Connection as Conn

_connection = Conn()


class BaseModel:
    _name: str

    def __init__(self):
        self._name = type(self).__name__

    def select(self):
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

    def update(self, data: dict, condition: str = None):
        _connection.update(self._name, data, condition)

    def __str__(self):
        attributes = type(self).__dict__['__annotations__']
        string = f"{type(self).__name__}("
        for attr in attributes.keys():
            string += f"{attr} : {self.__dict__[attr]}, "
        string += ')'
        return string
