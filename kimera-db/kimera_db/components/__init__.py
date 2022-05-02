import logging

from kimera_db.components.sqlalchemy.core import SQLAlchemyCore
from kimera_db.components.tools.sqlgenerator import sql_generator


def create_table_if_not_exist(source_data, dialect, driver_name, username, password, host, port, database,
                              table_name=None, default_dialect=None, save_metadata_to=None, metadata_source=None,
                              varying_length_text=False, uniques=False, pk_name=None, force_pk=False,
                              data_size_cushion=0, _parent_table=None, _fk_field_name=None, reorder=False,
                              loglevel=logging.WARN, limit=None, inserts=False, creates=True, query_list=False, *args,
                              **kwargs):
    # tools -> sql_generator
    sql_statement = sql_generator(source_data,
                                  table_name=table_name,
                                  default_dialect=default_dialect,
                                  save_metadata_to=save_metadata_to,
                                  metadata_source=metadata_source,
                                  varying_length_text=varying_length_text,
                                  uniques=uniques,
                                  pk_name=pk_name,
                                  force_pk=force_pk,
                                  data_size_cushion=data_size_cushion,
                                  _parent_table=_parent_table,
                                  _fk_field_name=_fk_field_name,
                                  reorder=reorder,
                                  loglevel=loglevel,
                                  limit=limit,
                                  dialect=dialect,
                                  inserts=inserts,
                                  creates=creates)

    # sqlalchemy -> core -> create_engine
    url = SQLAlchemyCore.create_url(driver_name=driver_name, username=username, password=password, host=host, port=port,
                                    database=database)
    engine = SQLAlchemyCore.create_engine(url, *args, **kwargs)

    if query_list:
        sql_statement = sql_statement.split(";")
        [engine.execute(q) for q in sql_statement]
    else:
        engine.execute(sql_statement)

    return engine
