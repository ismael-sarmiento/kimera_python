import logging
import unittest


class TestToolsUtilsLogger(unittest.TestCase):

    def setUp(self) -> None:
        self.kimera_logger = logging.getLogger('kimera-core-basic')

    def tearDown(self) -> None:
        print(self.shortDescription())

    def test_given_object_logger_set_message_type_info_then_print_message_success(self):
        self._testMethodDoc = "I - test_given_object_logger_set_message_type_info_then_print_message_success"

        self.kimera_logger.info(self._testMethodDoc)

        with self.assertLogs('kimera-core-basic', level=logging.INFO) as watcher:
            logging.getLogger('kimera-core-basic').info(self._testMethodDoc)
            self.assertEqual(watcher.output, self.kimera_logger.handlers[0].watcher.output)

    def test_given_object_logger_set_message_type_debug_then_print_message_success(self):
        self._testMethodDoc = "II - test_given_object_logger_set_message_type_debug_then_print_message_success"

        self.kimera_logger.info(self._testMethodDoc)

        with self.assertLogs('kimera-core-basic', level=logging.DEBUG) as watcher:
            logging.getLogger('kimera-core-basic').debug(self._testMethodDoc)
            self.assertEqual(watcher.output, self.kimera_logger.handlers[0].watcher.output)

    def test_given_object_logger_set_message_error_error_then_print_message_success(self):
        self._testMethodDoc = "III - test_given_object_logger_set_message_type_error_then_print_message_success"

        self.kimera_logger.info(self._testMethodDoc)

        with self.assertLogs('kimera-core-basic', level=logging.ERROR) as watcher:
            logging.getLogger('kimera-core-basic').error(self._testMethodDoc)
            self.assertEqual(watcher.output, self.kimera_logger.handlers[0].watcher.output)
