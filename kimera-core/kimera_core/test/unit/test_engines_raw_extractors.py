import unittest

from kimera_core.components.engines.raw.extractors import RawJsonExtractor


class TestEnginesRawExtractors(unittest.TestCase):

    def setUp(self) -> None:
        self.test_json_path_file = "path-to-json-file"
        self.string_json = """{"key":"value"}"""

    def tearDown(self) -> None:
        self._testMethodDoc = f"{self.__dict__['_testMethodName']}"
        print(self.shortDescription())

    def test_given_content_of_json_file_when_call_json_read_then_return_a_valid_dict(self):
        json_object = RawJsonExtractor().read(self.string_json)
        assert (isinstance(json_object, dict))
        assert (json_object.get("key") == "value")
