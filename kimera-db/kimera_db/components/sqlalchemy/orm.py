"""
    https://docs.sqlalchemy.org/en/13/orm/
"""
from sqlalchemy.orm import Session


class SQLAlchemyORM:

    @staticmethod
    def create_session(*args, **kwargs):
        """
            Documentation: https://docs.sqlalchemy.org/en/13/orm/session_api.html#sqlalchemy.orm.session.Session
                           https://docs.sqlalchemy.org/en/13/orm/session_basics.html#session-frequently-asked-questions

            Manages persistence operations for ORM-mapped objects.

            class sqlalchemy.orm.session.Session(bind=None, autoflush=True, expire_on_commit=True,
            _enable_transaction_accounting=True, autocommit=False, twophase=False, weak_identity_map=None,
            binds=None, extension=None, enable_baked_queries=True, info=None, query_cls=None)

        - autocommit: Defaults to False. When True, the Session does not keep a persistent transaction running,
        and will acquire connections from the engine on an as-needed basis, returning them immediately after
        their use. Flushes will begin and commit (or possibly rollback) their own transaction if no transaction
        is present. When using this mode, the Session.begin() method is used to explicitly start transactions. -
        - autoflush: When True, all query operations will issue a Session.flush() call to this Session before
        proceeding. This is a convenience feature so that Session.flush() need not be called repeatedly in order
        for database queries to retrieve results. It’s typical that autoflush is used in conjunction with
        autocommit=False. In this scenario, explicit calls to Session.flush() are rarely needed; you usually only
        need to call Session.commit() (which flushes) to finalize changes.
        - bind: An optional Engine or Connection to which this Session should be bound. When specified, all SQL
        operations performed by this session will execute via this connectable.
        - binds: A dictionary which may specify any number of Engine or Connection objects as the source of
        connectivity for SQL operations on a per-entity basis. The keys of the dictionary consist of any series of
        mapped classes, arbitrary Python classes that are bases for mapped classes, Table objects and Mapper
        objects. The values of the dictionary are then instances of Engine or less commonly Connection objects.
        Operations which proceed relative to a particular mapped class will consult this dictionary for the closest
        matching entity in order to determine which Engine should be used for a particular SQL operation. The
        complete heuristics for resolution are described at Session.get_bind(). Usage looks like:

        Session = sessionmaker(binds={SomeMappedClass: create_engine('postgresql://engine1'),
                                      SomeDeclarativeBase: create_engine('postgresql://engine2'),
                                      some_mapper: create_engine('postgresql://engine3'),
                                      some_table: create_engine('postgresql://engine4'),})

        - class_: Specify an alternate class other than sqlalchemy.orm.session.Session which should be used by the
        returned class. This is the only argument that is local to the sessionmaker function, and is not sent
        directly to the constructor for Session.
        - enable_baked_queries: defaults to True. A flag consumed by the sqlalchemy.ext.baked extension to determine
         if “baked queries” should be cached, as is the normal operation of this extension. When set to False, all
         caching is disabled, including baked queries defined by the calling application as well as those used
         internally. Setting this flag to False can significantly reduce memory use, however will also degrade
         performance for those areas that make use of baked queries (such as relationship loaders). Additionally,
         baked query logic in the calling application or potentially within the ORM that may be malfunctioning due
         to cache key collisions or similar can be flagged by observing if this flag resolves the issue.
        - expire_on_commit: Defaults to True. When True, all instances will be fully expired after each commit(),
        so that all attribute/object access subsequent to a completed transaction will load from the most recent
        database state.
        - info: optional dictionary of arbitrary data to be associated with this Session. Is available via the
        Session.info attribute. Note the dictionary is copied at construction time so that modifications to the
        per- Session dictionary will be local to that Session.
        - query_cls¶ – Class which should be used to create new Query objects, as returned by the Session.query()
        method. Defaults to Query.
        - twophase¶ – When True, all transactions will be started as a “two phase” transaction, i.e. using the
        “two phase” semantics of the database in use along with an XID. During a commit(), after flush() has been
        issued for all attached databases, the TwoPhaseTransaction.prepare() method on each database’s
        TwoPhaseTransaction will be called. This allows each database to roll back the entire transaction, before
        each transaction is committed.
        """
        return Session(*args, **kwargs)
