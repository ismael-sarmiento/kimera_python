""" This module contains different implementations of serializers """

import json
from abc import abstractmethod, ABC
from datetime import datetime, date


class KimeraEncoder(json.JSONEncoder):
    """ Subclass of json.JSONEncoder """

    def default(self, _object):
        """
            See at the documentation of the parent function.

        :param _object: Object to serialize.
        :return: Deserializable object or raise an exception.
        """
        serializer = KimeraSerializer()
        if serializer.can_any_advanced_serializer_handle_this_object(_object):
            return json.loads(serializer.serialize(_object))
        return super().default(_object)


class KimeraDecoder(json.JSONDecoder):
    """ Subclass of json.JSONDecoder """

    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    @staticmethod
    def __is_kimera_serializer_mode(_dict: object) -> bool:
        return 'serializer' in _dict and 'data' in _dict

    def object_hook(self, _object: dict) -> object:
        """
            See at the documentation of the parent function.

        ``object_hook``, if specified, will be called with the result
        of every JSON object decoded and its return value will be used in
        place of the given ``dict``.  This can be used to provide custom
        deserialization (e.g. to support JSON-RPC class hinting).
        :param _object: Object to deserialize.
        :return: Deserialized object.
        """
        if self.__is_kimera_serializer_mode(_object) and _object['serializer'] != DefaultSerializerHandler.__name__:
            return KimeraSerializer().deserialize(json.dumps(_object))
        return _object


class BaseSerializerHandler(ABC):
    """ Abstract class of serializer """

    @staticmethod
    def encoder_cls():
        """ JSONEncoder custom subclass """
        return KimeraEncoder

    @staticmethod
    def decoder_cls():
        """ JSONDecoder custom subclass """
        return KimeraDecoder

    @abstractmethod
    def can_i_handle_object_to_serialize(self, _object: object) -> bool:
        """
            Method that returns whether or not the class can handle the object to be serialized.

        :param _object: Object to serialize.
        :return: [bool] Serializable object or not.
        """

    @abstractmethod
    def can_i_handle_object_to_deserialize(self, _object: object) -> bool:
        """
            Method that returns whether or not the class can handle the object to be deserialized.

        :param _object: Object to deserialize.
        :return: [bool] Deserialized object or not.
        """

    @abstractmethod
    def build_serializer(self, _object):
        """
            Method to serialize an object.

        :param _object: Object to serialize.
        :return: [object] Serialize object.
        """

    @abstractmethod
    def build_deserializer(self, _object):
        """
            Method to deserialize an object.

        :param _object: Object to deserialize.
        :return: [object] Deserialize object.
        """


class DefaultSerializerHandler(BaseSerializerHandler):
    """ Default Serializer Handler """

    @staticmethod
    def __serialize_object(_object):
        return _object

    @staticmethod
    def __deserialize_object(_object):
        return _object

    def can_i_handle_object_to_serialize(self, _object):
        return True

    def can_i_handle_object_to_deserialize(self, _object: str) -> bool:
        return json.loads(_object)['serializer'] == self.__class__.__name__

    def build_serializer(self, _object):
        return json.dumps({'data': self.__serialize_object(_object), 'serializer': self.__class__.__name__}, cls=self.encoder_cls())

    def build_deserializer(self, _object):
        return self.__deserialize_object(json.loads(_object, cls=self.decoder_cls())['data'])


class ListSerializerHandler(BaseSerializerHandler):
    """ List Serializer Handler """

    @staticmethod
    def __serialize_object(_objects: list) -> list:
        return [KimeraSerializer().serialize(_object) for _object in _objects]

    @staticmethod
    def __deserialize_object(_objects: list) -> list:
        return [KimeraSerializer().deserialize(_object) for _object in _objects]

    def can_i_handle_object_to_serialize(self, _object):
        return isinstance(_object, list)

    def can_i_handle_object_to_deserialize(self, _object: str) -> bool:
        return json.loads(_object)['serializer'] == self.__class__.__name__

    def build_serializer(self, _object):
        return json.dumps({'data': self.__serialize_object(_object), 'serializer': self.__class__.__name__})

    def build_deserializer(self, _object):
        return self.__deserialize_object(json.loads(_object)['data'])


class TupleSerializerHandler(BaseSerializerHandler):
    """ Tuple Serializer Handler """

    @staticmethod
    def __serialize_object(_objects: tuple) -> tuple:
        return tuple(KimeraSerializer().serialize(_object) for _object in _objects)

    @staticmethod
    def __deserialize_object(_objects: tuple) -> tuple:
        return tuple(KimeraSerializer().deserialize(_object) for _object in _objects)

    def can_i_handle_object_to_serialize(self, _object):
        return isinstance(_object, tuple)

    def can_i_handle_object_to_deserialize(self, _object: str) -> bool:
        return json.loads(_object)['serializer'] == self.__class__.__name__

    def build_serializer(self, _object):
        return json.dumps({'data': self.__serialize_object(_object), 'serializer': self.__class__.__name__})

    def build_deserializer(self, _object):
        return self.__deserialize_object(json.loads(_object)['data'])


class DictSerializerHandler(BaseSerializerHandler):
    """ Dictionary Serializer Handler """

    @staticmethod
    def __serialize_object(_objects: dict) -> dict:
        return {key: KimeraSerializer().serialize(_objects[key]) for key in _objects}

    @staticmethod
    def __deserialize_object(_objects: dict) -> dict:
        return {key: KimeraSerializer().deserialize(_objects[key]) for key in _objects}

    def can_i_handle_object_to_serialize(self, _object):
        return isinstance(_object, dict)

    def can_i_handle_object_to_deserialize(self, _object: str) -> bool:
        return json.loads(_object)['serializer'] == self.__class__.__name__

    def build_serializer(self, _object):
        return json.dumps({'data': self.__serialize_object(_object), 'serializer': self.__class__.__name__})

    def build_deserializer(self, _object):
        return self.__deserialize_object(json.loads(_object)['data'])


class DateTimeSerializerHandler(BaseSerializerHandler):
    """ DateTime Serializer Handler """

    @staticmethod
    def __serialize_object(_object):
        return _object.strftime('%Y%m%d %H:%M:%S.%f')

    @staticmethod
    def __deserialize_object(_object):
        return datetime.strptime(_object, '%Y%m%d %H:%M:%S.%f')

    def can_i_handle_object_to_deserialize(self, _object: str) -> bool:
        return json.loads(_object)['serializer'] == self.__class__.__name__

    def can_i_handle_object_to_serialize(self, _object):
        return isinstance(_object, datetime)

    def build_serializer(self, _object):
        return json.dumps({'data': self.__serialize_object(_object), 'serializer': self.__class__.__name__})

    def build_deserializer(self, _object):
        return self.__deserialize_object(json.loads(_object)['data'])


class DateSerializerHandler(BaseSerializerHandler):
    """ Date Serializer Handler """

    @staticmethod
    def __serialize_object(_object):
        return _object.strftime('%Y%m%d')

    @staticmethod
    def __deserialize_object(_object):
        return datetime.strptime(_object, '%Y%m%d').date()

    def can_i_handle_object_to_deserialize(self, _object: str) -> bool:
        return json.loads(_object)['serializer'] == self.__class__.__name__

    def can_i_handle_object_to_serialize(self, _object):
        return isinstance(_object, date) and _object.__class__ == date

    def build_serializer(self, _object):
        return json.dumps({'data': self.__serialize_object(_object), 'serializer': self.__class__.__name__})

    def build_deserializer(self, _object):
        return self.__deserialize_object(json.loads(_object)['data'])


class KimeraSerializer:
    """ Composed class of serializers """

    def __init__(self):
        self.serializers = [DateSerializerHandler(), DateTimeSerializerHandler(), DictSerializerHandler(), TupleSerializerHandler(),
                            ListSerializerHandler(), DefaultSerializerHandler()]

    def get_serializer_from_object(self, _object):
        serializers = list(filter(lambda serializer: serializer.can_i_handle_object_to_serialize(_object), self.serializers))
        return serializers[0] if serializers else Exception(f'No se ha encontrado un serializador para este objeto: {_object}')

    def get_deserializer_from_object(self, _object):
        serializers = list(filter(lambda serializer: serializer.can_i_handle_object_to_deserialize(_object), self.serializers))
        return serializers[0] if serializers else Exception(f'No se ha encontrado un deserializador para este objeto: {_object}')

    def can_any_advanced_serializer_handle_this_object(self, _object):
        return any(list(filter(lambda serializer: serializer.can_i_handle_object_to_serialize(_object), self.serializers[:-1])))

    def serialize(self, _object):
        return self.get_serializer_from_object(_object).build_serializer(_object)

    def deserialize(self, _object):
        return self.get_deserializer_from_object(_object).build_deserializer(_object)
