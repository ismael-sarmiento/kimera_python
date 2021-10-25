import unittest

from kimera_core.components.engines.raw.extractors import RawJsonExtractor


class TestEnginesRawExtractors(unittest.TestCase):

    def setUp(self) -> None:
        self.test_json_content = """
        {
          "spark-config": {
            "mode": "Master",
            "master-url": "localhost:9000"
          }
        }
        """

    def tearDown(self) -> None:
        self._testMethodDoc = f"{self.__dict__['_testMethodName']}"
        print(self.shortDescription())

    def test_given_content_of_json_file_when_call_json_read_then_return_a_valid_dict(self):
        json_file_content = RawJsonExtractor().read_from_json_content(self.test_json_content)
        assert (isinstance(json_file_content, dict))
