import re
import unittest

from kimera_db.components.tools.sqlgenerator import sql_generator
from kimera_db.test import get_resource_file


class TestSQLGenerator(unittest.TestCase):

    def setUp(self) -> None:
        self.filename = "covid-variants.csv"
        self.resource_file = get_resource_file(self.filename)

    def tearDown(self) -> None:
        print(self.id())

    def test_given_data_as_file_path_when_execute_sql_generator_function_then_return_valid_sql_statement(self):
        """
        Convert a data as string with path format to valid sql statement ( postgres )
        """
        regex = r"[-.]"
        table_name = re.sub(regex, "#", self.filename)
        sql_statement = sql_generator(self.resource_file, table_name=table_name, dialect="postgresql", limit=100)

        assert isinstance(sql_statement, str)
        assert self.filename not in sql_statement
        assert table_name in sql_statement
        assert len(sql_statement) > 300
