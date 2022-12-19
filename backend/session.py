from sqlalchemy import create_engine


def get_session():
    engine = create_engine("postgresql+psycopg2://postgres:postgres@192.168.249.28/library", echo=True)
    conn = engine.connect()
    return conn


def check_connection(connection):
    try:
        connection.execute("SELECT VERSION()")
        result = connection.fetchone()
    except Exception as er:
        print(er)
        connection = get_session()
    finally:
        return connection
