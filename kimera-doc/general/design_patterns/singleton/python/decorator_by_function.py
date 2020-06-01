from abc import ABC


# decorator by function
def singleton_decorator_by_function(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            print(f"\tCreando la clase '{class_.__name__}' desde el decorador singleton por función.")
            instances[class_] = class_(*args, **kwargs)  # se llama al built-in __new__ de la clase
        return instances[class_]

    return get_instance


class BaseClass(ABC):

    def __init__(self):
        print(f"\tInicializando la clase '{self.__class__.__base__.__name__}'")
        self.super_count = 1


@singleton_decorator_by_function
class MyClass(BaseClass):

    def get_info(self):
        print(f"\tSe ha realizado una llamada a la subclase '{self.__class__.__name__}' con id: {id(self.__class__)}. "
              f"Hereda de la clase '{self.__class__.__base__.__name__}' con id {id(self.__class__.__base__)}.")

    def __init__(self):
        super().__init__()
        print(f"\tInicializando la clase '{self.__class__.__name__}'")
        self.count = 1
        self.get_info()

    def counter(self):
        print("\tAccediendo al método al 'counter' correctamente.")
        self.count += 1
        return self.count


class Ismael: pass


if __name__ == '__main__':
    # singleton_decorator_by_function
    print("SINGLETON PATTERN: DECORATOR BY FUNCTION")
    print("\nCreando instancias  'm' y 'n' de MyClass.")
    m = MyClass()
    n = MyClass()
    print(f"id(m) == id(MyClass()): {id(m) == id(MyClass())}")  # 'm' es una clase singleton
    print(f"id(m) == id(n): {id(m) == id(n)}")  # 'm' y 'n' son clases singleton
    print(f"type(m)() == type(MyClass())(): {type(m)() == type(MyClass())()}")  # TODO: No entiendo esto
    print(f"Accediendo a los métodos de la clase '{n.__class__.__name__}'")
    count = n.counter()
