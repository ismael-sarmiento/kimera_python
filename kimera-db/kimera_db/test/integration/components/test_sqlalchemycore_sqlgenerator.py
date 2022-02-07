import re
import unittest

from kimera_db.components import create_table_if_not_exist
from kimera_db.components.sqlalchemy.core import SQLAlchemyCore
from kimera_db.components.tools.sqlgenerator import sql_generator
from kimera_db.test import get_resource_file


class TestSQLAlchemyCoreSQLGenerator(unittest.TestCase):

    def setUp(self) -> None:
        self.filename = "covid-variants.csv"
        self.resource_file = get_resource_file(self.filename)

    def tearDown(self) -> None:
        print(self.id())

    def test_given_resource_file_when_execute_sql_generator_and_create_engine_functions_then_return_valid_response(
            self):
        # tools -> sql_generator
        regex = r"[-.]"
        table_name = re.sub(regex, "_", self.filename)
        sqlite_dialect = "sqlite"
        sql_statement = sql_generator(
            self.resource_file,
            table_name=table_name,
            dialect=sqlite_dialect,
            limit=100,
            inserts=True
        )

        assert isinstance(sql_statement, str)
        assert self.filename not in sql_statement
        assert table_name in sql_statement
        assert "DROP" in sql_statement
        assert "CREATE" in sql_statement
        assert "INSERT" in sql_statement
        assert len(sql_statement) > 300

        # sqlalchemy -> core -> create_engine
        mock_url: str = "sqlite:///:memory:"
        creation_query: list = sql_statement.split(";")
        validator_query: str = f"SELECT * FROM {table_name};"

        sqlite_engine = SQLAlchemyCore.create_engine(mock_url)

        [sqlite_engine.execute(q) for q in creation_query]

        result = sqlite_engine.execute(validator_query).all()
        assert isinstance(result, list)
        assert len(result) == 100

    def test_given_valid_parameters_when_execute_create_table_if_not_exist_function_then_return_valid_response(self):
        sqlite_dialect = "sqlite"
        regex = r"[-.]"
        table_name = re.sub(regex, "", self.filename)
        validator_query: str = f"SELECT * FROM {table_name};"
        sqlite_engine = create_table_if_not_exist(
            source_data=self.resource_file,
            dialect=sqlite_dialect,
            driver_name=sqlite_dialect,
            username="",
            password="",
            host="",
            port=None,
            database="",
            limit=100,
            query_list=True,
            table_name=table_name
        )
        result = sqlite_engine.execute(validator_query).all()
        assert isinstance(result, list)
        assert len(result) == 0
