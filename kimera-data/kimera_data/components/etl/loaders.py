from typing import List, Iterable

from kimera_core.components.tools.utils.generic import ExceptionsUtils, ObjectUtils, ImportUtils


class ETLLoader:

    def __init__(self):
        self._relations = dict()
        self._input = None
        self._loaders = list()
        self._cascade = False

    def input_data(self, *args, **kwargs):
        self._input = args, kwargs
        return self

    def apply(self, *args):
        self._relations = {'data': self._input, 'loader_object': args}
        return self

    def apply_in_cascade(self, *args):
        self._cascade = True
        self._relations = {'data': self._input, 'loader_object': args}
        return self

    def load(self):
        if self._i_can_load() and ImportUtils.attribute_exist(self, '_loaders') and self._loaders:
            return self._multi_load()
        else:
            return self._single_load()

    def _i_can_load(self):
        ExceptionsUtils.raise_exception_if_attr_not_defined(self, '_relations')
        return True

    def _single_load(self):
        input_data = self._relation_data()
        loader_object = self._relation_loader()
        return self._single_load_in_cascade(input_data, loader_object) if self._cascade else \
            self._single_loader(input_data, loader_object)

    def _relation_data(self):
        if ImportUtils.attribute_exist(self, '_relations') and self._relations and 'data' in self._relations:
            return self._relations['data']

    def _relation_loader(self):
        if ImportUtils.attribute_exist(self, '_relations') and self._relations and 'loader_object' in self._relations:
            return self._relations['loader_object']

    def _single_load_in_cascade(self, input_data, loader_object):
        data = None
        for loader in loader_object:
            input_data = self._load_data(input_data, loader)
            data = input_data
            input_data = tuple([[input_data], {}])
        return data

    def _single_loader(self, input_data, loader_object):
        return [self._load_data(input_data, loader) for loader in loader_object]

    @staticmethod
    def _load_data(input_data, loader):
        data = loader(*input_data[0], **input_data[1])
        return data

    def _multi_load(self):
        return [loader.load() for loader in self._loaders]

    def multiple(self, loaders: Iterable[List['ETLLoader']]):
        if not (loaders and ObjectUtils.internal_objects_of_iterable_are_instances_of_class(loaders, ETLLoader)
                and ObjectUtils.object_is_instance_of_class(loaders, list)):
            raise TypeError("Input parameters must be of type ETLLoader 'list'.")
        self._loaders = loaders
        return self

    def clear(self):
        self._relations = dict()
        self._input = None
        self._loaders = list()
        self._cascade = False
