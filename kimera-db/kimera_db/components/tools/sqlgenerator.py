import logging

from ddlgenerator.ddlgenerator import Table

__all__ = ["sql_generator"]


def sql_generator(source_data, dialect, table_name=None, default_dialect=None, save_metadata_to=None,
                  metadata_source=None,
                  varying_length_text=False, uniques=False, pk_name=None, force_pk=False, data_size_cushion=0,
                  _parent_table=None, _fk_field_name=None, reorder=False, loglevel=logging.WARN, limit=None,
                  inserts=False, creates=True):
    """
    Return a sql statement as text
    """
    sql_generator_text = Table(source_data,
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
                               limit=limit).sql(dialect=dialect,
                                                inserts=inserts,
                                                creates=creates)
    return sql_generator_text
