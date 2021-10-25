import logging
import unittest


class TestToolsUtilsLogger(unittest.TestCase):

    def setUp(self) -> None:
        self.kimera_logger = logging.getLogger('kimera-core-basic')

    def tearDown(self) -> None:
        self._testMethodDoc = f"{self.__dict__['_testMethodName']}"
        print(self.shortDescription())

    def test_given_object_logger_set_message_type_info_then_print_message_success(self):
        self.kimera_logger.info(self.id())

        with self.assertLogs('kimera-core-basic', level=logging.INFO) as watcher:
            logging.getLogger('kimera-core-basic').info(self.id())
            self.assertEqual(watcher.output, self.kimera_logger.handlers[0].watcher.output)

    def test_given_object_logger_set_message_type_debug_then_print_message_success(self):
        self.kimera_logger.info(self.id())

        with self.assertLogs('kimera-core-basic', level=logging.DEBUG) as watcher:
            logging.getLogger('kimera-core-basic').debug(self.id())
            self.assertEqual(watcher.output, self.kimera_logger.handlers[0].watcher.output)

    def test_given_object_logger_set_message_error_error_then_print_message_success(self):
        self.kimera_logger.info(self.id())

        with self.assertLogs('kimera-core-basic', level=logging.ERROR) as watcher:
            logging.getLogger('kimera-core-basic').error(self.id())
            self.assertEqual(watcher.output, self.kimera_logger.handlers[0].watcher.output)
