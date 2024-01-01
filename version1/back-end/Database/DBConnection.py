import os

from psycopg import connect, OperationalError


class DBConnection:

    @staticmethod
    def db_connection():
        try:
            new_connection = connect(
                host=os.environ.get("HOST"),
                dbname=os.environ.get("DBNAME"),
                user=os.environ.get("USER"),
                password=os.environ.get("PASSWORD"),
                port=os.environ.get("PORT")
            )
            return new_connection
        except OperationalError:
            raise OperationalError("Could not connect to the database, please try again!")

connection = DBConnection.db_connection()
print("Successfully connected to the database!")
