from Database.DBConnection import DBConnection


def drop_table(table_name):
    connection = DBConnection.db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(f"DROP TABLE IF EXISTS 143Designs.{table_name};")
        connection.commit()
        print(f"{table_name} table dropped successfully!")
    except Exception as error:
        print(f"Error dropping {table_name} table: {str(error)}")

    try:
        cursor.execute("DROP SCHEMA IF EXISTS 143Designs CASCADE;")
        connection.commit()
        print("Schema successfully dropped")
    except Exception as error:
        print(f"Error dropping schema: {str(error)}")

if __name__ == "__main__":
    tables_to_drop = ["User", "Session", "Request", "Review", "Work"]
    for table in tables_to_drop:
        drop_table(table)
