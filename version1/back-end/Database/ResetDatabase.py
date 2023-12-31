import bcrypt

from Database.DBConnection import DBConnection


connection = DBConnection.db_connection()
cursor = connection.cursor()

def truncate_table(table_name):
    try:
        cursor.execute(f"TRUNCATE TABLE Designs.{table_name} RESTART IDENTITY CASCADE;")
        connection.commit()
        print(f"{table_name} truncated successfully!")
    except Exception as error:
        print(f"Error truncating {table_name}: {str(error)}")

if __name__ == "__main__":
    tables_to_restart = ["User", "Order", "Session", "Request", "Review", "Work", "Item"]

    for table in tables_to_restart:
        truncate_table(table)

    password = bcrypt.hashpw("test".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    cursor.execute(f"INSERT INTO Designs.User (user_id, email, passwrd) VALUES (-1, 'test@email.com', %s);",
                   (password,))
    cursor.execute("INSERT INTO Designs.User (user_id, email, passwrd) VALUES (-2, "
                   "'delete-all-sessions@email.com', 'test');")
    cursor.execute("INSERT INTO Designs.Session (session_id, user_id, expiration) "
                   "VALUES ('-1', -1, '2022-1-1 1:30:45');")
    cursor.execute("INSERT INTO Designs.Session (session_id, user_id, expiration) "
                   "VALUES ('-2', -1, '2029-1-1 1:30:45');")
    cursor.execute("INSERT INTO Designs.Session (session_id, user_id, expiration) "
                   "VALUES ('-3', -1, '2029-1-1 1:30:45');")
    connection.commit()
    connection.close()
