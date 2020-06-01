# Design Patterns

Los patrones de diseño proporcionan soluciones a los **"commonly occurring problems"** en el diseño de software. Los patrones de diseño fueron introducidos 
por primera vez por **GoF(Gang of Four)** donde describían los patrones comunes como problemas que ocurren una y otra vez y soluciones a esos problemas.

Los patrones de diseño tienen cuatro elementos esenciales:
* **The pattern name** - es un identificador que podemos usar para describir un problema de diseño, sus soluciones y consecuencias en una o dos palabras.
* **The problem** - describe cuándo aplicar el patrón.
* **The solution** - describe los elementos que conforman el diseño, sus relaciones, responsabilidades y colaboraciones.
* **The consequences** - son los resultados y las compensaciones de aplicar el patrón.

Las ventajas de los patrones de diseño son:
* Son reutilizables en múltiples proyectos.
* El nivel arquitectónico de problemas puede ser resuelto.
* Han sido probados y probados con el tiempo, lo cual es la experiencia de desarrolladores y arquitectos.
* Tienen confiabilidad y dependencia.

Los patrones de diseño se pueden clasificar en categorías:
* **Creational Pattern** : se ocupan de cómo se puede crear el objeto y aíslan los detalles de la creación del objeto.
* **Structural Pattern** : diseñan la estructura de clases y objetos para que puedan componerse para lograr resultados más grandes.
* **Behavioral Pattern** : se ocupan de la interacción entre los objetos y la responsabilidad de los objetos.

## Creational Patterns

### Singleton

_**Garantiza que una clase sólo tenga una instancia, y proporciona un punto de acceso global a ella.**_

#### Casos de uso
* Operaciones de base de datos, donde queremos que el objeto de la base de datos mantenga la consistencia de los datos.

#### Implementations
##### Python

---
* [Reference Link](https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python)
---
* A decorator by function
    * Pros
        * Los decoradores son aditivos de una manera que a menudo es más intuitiva que la herencia múltiple
    * Cons
        * Si bien los objetos creados con MyClass() serían verdaderos objetos singleton, MyClass en sí es una función, no una clase, 
        por lo que no puede llamar a los métodos de clase desde ella. 
        También para m = MyClass (); n = MyClass (); o = tipo (n) (); entonces m == n && m! = o && n! = o
            * ``DUDA: tengo un ejemplo en el que si puedo acceder a los metodos. Pero sigo sin entender el por que m! = o && n! = o`` 
````python
# decorator by function
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance
````

* A base class
    * Pros
        * Es una verdadera clase
    * Cons
        * Herencia múltiple - ¡eugh! ¿`__new__` podría sobrescribirse durante la herencia de una segunda clase base? Uno tiene que pensar más de
         lo necesario.
```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
```
* A metaclass
    * Pros
        * Es una verdadera clase
        * Auto-mágicamente cubre la herencia
        * Utiliza `_metaclass__` para su propósito apropiado
    * Cons
        * Ni idea
```python
# metaclass 1: probada
class Singleton1(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton1, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)

# metaclass 2: sin probar
class Singleton2(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args,**kw)
        return cls.__instance


class BaseClass: pass

#Python2
class MyClass2(BaseClass):
    __metaclass__ = Singleton1

#Python3
class MyClass3(BaseClass, metaclass=Singleton1):
    pass
```

* Decorator returning a class with the same nam
    * Pros
        
    * Cons
        
```python
def singleton(cls):
    class class_w(cls):
        _instance = None
        def __new__(cls, *args, **kwargs):
            if class_w._instance is None:
                class_w._instance = super(class_w,
                                    cls).__new__(cls,
                                                    *args,
                                                    **kwargs)
                class_w._instance._sealed = False
            return class_w._instance
        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True
    class_w.__name__ = cls.__name__
    return class_w

class BaseClass: pass

@singleton
class MyClass(BaseClass):
    pass
```
* A module file

        a module file singleton.py

    * Pros
        * Simple is better than complex
    * Cons
        * Ni idea

