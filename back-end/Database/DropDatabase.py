from Database.DBConnection import DBConnection


def drop_table(table_names):
    connection = DBConnection.db_connection()
    cursor = connection.cursor()

    for table_name in table_names:
        try:
            cursor.execute(f"DROP TABLE IF EXISTS Designs.{table_name};")
            connection.commit()
            print(f"{table_name} table dropped successfully!")
        except Exception as error:
            print(f"Error dropping {table_name} table: {str(error)}")
    try:
        cursor.execute("DROP SCHEMA IF EXISTS Designs CASCADE;")
        connection.commit()
        print("Schema successfully dropped")
    except Exception as error:
        print(f"Error dropping schema: {str(error)}")

if __name__ == "__main__":
    drop_table(["Session", "Order", "User", "Request", "Review", "Work", "Item"])
