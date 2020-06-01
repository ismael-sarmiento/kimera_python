# Metaclass
class Singleton1(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton1, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)


class Singleton2(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance


class BaseClass:

    def __init__(self, my_count):
        print(f"\tInicializando la clase '{self.__class__.__base__.__name__}'")
        self.super_count = my_count


class MyClass(BaseClass, metaclass=Singleton2):

    @classmethod
    def get_info(cls):
        print(f"\tSe ha realizado una llamada a la subclase '{cls.__class__.__name__}' con id: {id(cls.__class__)}. "
              f"Hereda de la clase '{cls.__class__.__base__.__name__}' con id {id(cls.__class__.__base__)}.")

    def __init__(self, my_count):
        super().__init__(my_count)
        print(f"\tInicializando la clase '{self.__class__.__name__}'")
        self.count = my_count
        self.get_info()

    def counter(self):
        print("\tAccediendo al método al 'counter' correctamente.")
        self.count += 1
        return self.count


if __name__ == '__main__':
    # singleton_decorator_by_function
    print("SINGLETON PATTERN: BY INHERITANCE")
    print("\nCreando instancias  'm' y 'n' de MyClass.")
    m = MyClass(5)
    n = MyClass(7)
    print(f"id(m) == id(MyClass()): {id(m) == id(MyClass(3))}")  # 'm' es una clase singleton
    print(f"id(m) == id(n): {id(m) == id(n)}")  # 'm' y 'n' son clases singleton
    print(f"type(m)() == type(MyClass(3))(8): {type(m)(6) == type(MyClass(3))(8)}")  # TODO: No entiendo esto
    print(f"Accediendo a los métodos de la clase '{n.__class__.__name__}'")
    count = n.counter()
