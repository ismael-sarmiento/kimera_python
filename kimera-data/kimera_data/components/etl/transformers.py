from typing import List, Iterable

from kimera_core.components.tools.utils.generic import ExceptionsUtils, ObjectUtils, ImportUtils


class ETLTransformer:

    def __init__(self):
        self._relations = dict()
        self._input = None
        self._transformers = list()
        self._cascade = False

    def input_data(self, *args, **kwargs):
        self._input = args, kwargs
        return self

    def apply(self, *args):
        self._relations = {'data': self._input, 'transforming_object': args}
        return self

    def apply_in_cascade(self, *args):
        self._cascade = True
        self._relations = {'data': self._input, 'transforming_object': args}
        return self

    def transform(self):
        if self._i_can_transform() and ImportUtils.attribute_exist(self, '_transformers') and self._transformers:
            return self._multi_transform()
        else:
            return self._single_transform()

    def _i_can_transform(self):
        ExceptionsUtils.raise_exception_if_attr_not_defined(self, '_relations')
        return True

    def _single_transform(self):
        input_data = self._relation_data()
        transforming_object = self._relation_transformer()
        return self._single_transform_in_cascade(input_data, transforming_object) if self._cascade else \
            self._single_transformers(input_data, transforming_object)

    def _relation_data(self):
        if ImportUtils.attribute_exist(self, '_relations') and self._relations and 'data' in self._relations:
            return self._relations['data']

    def _relation_transformer(self):
        if ImportUtils.attribute_exist(self, '_relations') and self._relations and 'transforming_object' in self._relations:
            return self._relations['transforming_object']

    def _single_transform_in_cascade(self, input_data, transforming_object):
        data = None
        for transformer in transforming_object:
            input_data = self._transform_data(input_data, transformer)
            data = input_data
            input_data = tuple([[input_data], {}])
        return data

    def _single_transformers(self, input_data, transforming_object):
        return [self._transform_data(input_data, transformer) for transformer in transforming_object]

    @staticmethod
    def _transform_data(input_data, transformer):
        data = transformer(*input_data[0], **input_data[1])
        return data

    def _multi_transform(self):
        return [transformer.transform() for transformer in self._transformers]

    def multiple(self, transformers: Iterable[List['ETLTransformer']]):
        if not (transformers and ObjectUtils.internal_objects_of_iterable_are_instances_of_class(transformers, ETLTransformer)
                and ObjectUtils.object_is_instance_of_class(transformers, list)):
            raise TypeError("Input parameters must be of type ETLTransformer 'list'.")
        self._transformers = transformers
        return self

    def clear(self):
        self._relations = dict()
        self._input = None
        self._transformers = list()
        self._cascade = False
