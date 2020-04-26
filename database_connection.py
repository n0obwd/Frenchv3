import psycopg2
from config import config


def db_connect(func):
    def connect(command,result):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()

            # execute a statement
            cur.execute(command)

            # display the PostgreSQL database server version
            result = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            result = []
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return func(command, result)
    return connect


@db_connect
def command(commandStr, result):
    return result


if __name__ == '__main__':
    myStr = "SELECT * FROM subject_pronouns"
    command(myStr, 'a')