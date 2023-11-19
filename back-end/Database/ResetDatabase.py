from datetime import timedelta, datetime

from Database.DBConnection import DBConnection


connection = DBConnection.db_connection()
cursor = connection.cursor()

def truncate_table(table_name):
    try:
        cursor.execute(f"TRUNCATE TABLE 143Designs.{table_name} RESTART IDENTITY CASCADE;")
        connection.commit()
        print(f"{table_name} truncated successfully!")
    except Exception as error:
        print(f"Error truncating {table_name}: {str(error)}")

if __name__ == "__main__":
    tables_to_restart = ["User", "Session", "Request", "Review", "Work"]

    for table in tables_to_restart:
        truncate_table(table)

    cursor.execute("INSERT INTO 143Designs.User (user_id, email, passwrd) VALUES (-1, 'test@email.com', 'test');")
    cursor.execute("INSERT INTO 143Designs.User (user_id, email, passwrd) VALUES (-2, "
                   "'delete-all-sessions@email.com', 'test');")
    cursor.execute(f"INSERT INTO 143Designs.Session (session_id, user_id, expiration) VALUES (-1, -1, "
                   f"{datetime.now() - timedelta(minutes=15)});")
    connection.commit()
    connection.close()
