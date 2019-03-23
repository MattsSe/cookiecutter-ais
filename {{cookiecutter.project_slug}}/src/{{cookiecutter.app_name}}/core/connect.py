{%- if cookiecutter.postgres %}
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from .logger import logger
{%- endif %}


{%- if cookiecutter.postgres %}
DATABASE_CONFIG = {
    'host': 'localhost',
    'db_name': 'company',
    'user': 'user',
    'password': 'password',
    'port': 5432
}
{%- endif %}
{%- if cookiecutter.postgres %}


def pg_connection_string(db_name=DATABASE_CONFIG['db_name'], host=DATABASE_CONFIG['host'], user=DATABASE_CONFIG['user'],
                         password=DATABASE_CONFIG['password'], port=DATABASE_CONFIG['port']):
    """
    constructs the database connection string
    :param db_name: the name of the database
    :param host: the ip of the host
    :param user: the username to access the database
    :param password: the password to gain access, if required
    :param port: the port of the running
    :return: a new postgres connection string
    """
    if password:
        password = ':' + password
    return f"postgresql://{user}{password}@{host}:{port}/{db_name}"


def create_engine_session(db_name=DATABASE_CONFIG['db_name'], host=DATABASE_CONFIG['host'], user=DATABASE_CONFIG['user'],
                         password=DATABASE_CONFIG['password'], port=DATABASE_CONFIG['port']):
    """
    initializes the sqlalchemy environment by setting up engine and session
    :param db_name: the name of the database to connect with
    :param db_name: the name of the database
    :param host: the ip of the host
    :param user: the username to access the database
    :param password: the password to gain access, if required
    :param port: the port of the running
    :return: a new sqlalchemy engine and session
    """
    engine = sa.create_engine(pg_connection_string(db_name, host, user, password, port))
    engine.connect()
    logger.debug(f"connected sqlalchemeny engine to '{db_name}'")
    Session = sessionmaker(bind=engine)
    session = Session()
    logger.debug(f"created new orm session sqlalchemy for {db_name} on {host}")
    return engine, session
{%- endif %}
