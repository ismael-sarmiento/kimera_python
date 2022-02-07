import unittest

from sqlalchemy.engine import URL

from kimera_db.components.sqlalchemy.core import SQLAlchemyCore


class TestSQLAlchemyCore(unittest.TestCase):

    def setUp(self) -> None:
        self.driver_name = "postgresql"
        self.username = "my_username"
        self.password = "****"
        self.host = "my_localhost"
        self.port = 5432
        self.database = "my_db"

    def tearDown(self) -> None:
        print(self.id())

    def test_given_valid_parameters_when_execute_create_url_function_then_return_valid_url(self):
        url = SQLAlchemyCore.create_url(driver_name=self.driver_name, username=self.username, password=self.password,
                                        host=self.host, port=self.port, database=self.database)

        assert isinstance(url, URL)
        assert self.driver_name in url
        assert self.username in url
        assert self.password in url
        assert self.host in url
        assert self.port in url
        assert self.database in url

    def test_given_mock_url_when_execute_create_engine_function_then_return_valid_engine(self):
        mock_url: str = "sqlite:///:memory:"
        table_name: str = "users"
        creation_query = [f"DROP TABLE IF EXISTS {table_name};",
                          f"CREATE TABLE {table_name} (id INTEGER NOT NULL,name VARCHAR(20),surname VARCHAR(20));",
                          f"INSERT INTO {table_name}(id, name) VALUES(1, 'albert');"]

        validator_query = f"SELECT * FROM {table_name};"

        sqlite_engine = SQLAlchemyCore.create_engine(mock_url)

        [sqlite_engine.execute(q) for q in creation_query]

        result = sqlite_engine.execute(validator_query).all()
        assert isinstance(result, list)
        assert len(result) == 1
        assert result == [(1, 'albert', None)]
