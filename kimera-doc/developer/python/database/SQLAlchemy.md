# SQLAlchemy

## SQLAlchemy Core

## SQLAlchemy ORM
### Connection Pooling

* [Reference Link](https://docs.sqlalchemy.org/en/13/core/pooling.html)

A connection pool is a standard technique used to maintain long running connections in memory for efficient re-use, 
as well as to provide management for the total number of connections an application might use simultaneously.

Particularly for server-side web applications, a connection pool is the standard way to maintain a “pool” of active 
database connections in memory which are reused across requests.

SQLAlchemy includes several connection pool implementations which integrate with the Engine.


