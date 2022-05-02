"""
    https://docs.sqlalchemy.org/en/13/core/
"""

from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.engine.url import make_url, URL


class SQLAlchemyCore:
    URL_STRUCTURE = "{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}"

    @staticmethod
    def create_engine(url, *args, **kwargs):
        """
            Documentation: https://docs.sqlalchemy.org/en/13/core/engines.html#sqlalchemy.create_engine

            The create_engine() function produces an Engine object based on a URL.
            These URLs follow RFC-1738, and usually can include:

            url_structure: dialect+driver://username:password@host:port/database

        - username: The username to database access.
        - password: database password.
        - host: The name of the host.
        - port: The port number.
        - database: The database name. (optional)
        - query: A dictionary of options to be passed to the dialect and/or the DBAPI upon connect. (optional)
        """
        return create_engine(url, *args, **kwargs)

    @staticmethod
    def create_engine_from_config(configuration: dict, prefix: str = 'sqlalchemy.', **kwargs):
        """
            Documentation: https://docs.sqlalchemy.org/en/13/core/engines.html#sqlalchemy.engine_from_config

            Create a new Engine instance using a configuration dictionary.

            The dictionary is typically produced from a config file.

            The keys of interest to engine_from_config() should be prefixed, e.g. sqlalchemy.url, sqlalchemy.echo, etc.
            The ‘prefix’ argument indicates the prefix to be searched for. Each matching key (after the prefix is
            stripped) is treated as though it were the corresponding keyword argument to a create_engine() call.

            The only required key is (assuming the default prefix) sqlalchemy.url, which provides the database URL.

            A select set of keyword arguments will be “coerced” to their expected type based on string values. The set
            of arguments is extensible per-dialect using the engine_config_types accessor.

        - configuration: A dictionary (typically produced from a config file, but this is not a requirement).
        Items whose keys start with the value of ‘prefix’ will have that prefix stripped, and will then be passed
        to create_engine.
        - prefix: Prefix to match and then strip from keys in ‘configuration’.
        - kwargs: Each keyword argument to engine_from_config() itself overrides the corresponding item taken from
        the ‘configuration’ dictionary. Keyword arguments should not be prefixed.
        """
        return engine_from_config(configuration, prefix, **kwargs)

    @staticmethod
    def make_url(name_or_url):
        """
            Documentation: https://docs.sqlalchemy.org/en/13/core/engines.html#sqlalchemy.engine.url.make_url

            Given a string or unicode instance, produce a new URL instance.

            The given string is parsed according to the RFC 1738 spec. If an existing URL object is passed,
            just returns the object.
        """
        return make_url(name_or_url)

    @staticmethod
    def create_url(driver_name, username=None, password=None, host=None, port=None, database=None, query=None):
        """
            Documentation: https://docs.sqlalchemy.org/en/13/core/engines.html#sqlalchemy.engine.url.URL

            Represent the components of a URL used to connect to a database.

            This object is suitable to be passed directly to a create_engine() call. The fields of the URL are parsed
            from a string by the make_url() function. The string format of the URL is an RFC-1738-style string.

            All initialization parameters are available as public attributes.

            drivername – the name of the database backend. This name will correspond to a module in sqlalchemy/databases
            or a third party plug-in.
                - firebird
                - mssql
                - mysql
                - postgresql
                - sqlite
                - oracle
                - sybase

        - username: The user name.
        - password: database password.
        - host: The name of the host.
        - port: The port number.
        - database: The database name. (optional)
        - query: A dictionary of options to be passed to the dialect and/or the DBAPI upon connect. (optional)
        """
        return URL.create(driver_name, username, password, host, port, database, query)
