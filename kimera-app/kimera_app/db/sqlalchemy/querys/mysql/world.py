from kimera_app.db.sqlalchemy.models.mysql.schemas.world import Sample
from kimera_db.components.sqlalchemy.core import SQLAlchemyCore
from kimera_db.components.sqlalchemy.orm import SQLAlchemyORM

url_mysql = SQLAlchemyCore.create_url(drivername="mysql",
                                      username="root",
                                      password="Maximus.Ismael.1993",
                                      host="localhost",
                                      port="3306",
                                      database="world")
engine_mysql = SQLAlchemyCore.create_engine(url_mysql, echo=True)
session_mysql = SQLAlchemyORM.create_session(bind=engine_mysql)

countries = session_mysql.query(Sample).all()

print(countries)
