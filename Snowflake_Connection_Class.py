from snowflake.connector import *
from sqlalchemy import *
#from sqlalch import results


class SnowFirst:
    sfAccount = 'ax60806.canada-central.azure'
    sfUser = 'XXXXXXXX'
    sfPswd = 'XXXXXX00'

    @staticmethod
    def test_db_connection():
        eagerest = create_engine('snowflake://{user}:{password}@{account}/'.format(
            user=SnowFirst.sfUser,
            password=SnowFirst.sfPswd,
            account=SnowFirst.sfAccount, ))
        try:
            connection = eagerest.connect()
            res = connection.execute('select current_version()').fetchone()
            connection.close()
            print('Connecton test is successful')
        except DatabaseError as exc:
            error, = exc.args
            print("Oracle-Error-Code:", error.code)
            print("Oracle-Error-Message:", error.message)
        finally:
            eagerest.dispose()


    # make db connection
    @staticmethod
    def make_db_connection():
        global con
        try:
            con = connect(
                user=SnowFirst.sfUser,
                password=SnowFirst.sfPswd,
                account=SnowFirst.sfAccount, )
        except DatabaseError as exc:
            error, = exc.args
            print("Oracle-Error-Code:", error.code)
            print("Oracle-Error-Message:", error.message)
        except InterfaceError as exc:
            error, = exc.args
            print("Oracle-Error-Code:", error.code)
            print("Oracle-Error-Message:", error.message)
        except InternalError as exc:
            error, = exc.args
            print("Oracle-Error-Code:", error.code)
            print("Oracle-Error-Message:", error.message)

        finally:
            return con
