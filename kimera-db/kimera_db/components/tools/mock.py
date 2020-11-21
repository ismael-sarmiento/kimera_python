from kimera_db.components.sqlalchemy.core import create_engine


def mock_engine():
    """
        Documentation: [Tutorial] https://docs.sqlalchemy.org/en/13/orm/tutorial.html#creating-a-session
    """
    MOCK_URL = "sqlite:///:memory:"
    return create_engine(MOCK_URL, echo=True)
