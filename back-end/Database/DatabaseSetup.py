from datetime import timedelta, datetime

from Database.DBConnection import DBConnection


def create_data(sql, data_name):
    connection = DBConnection.db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(sql)
        connection.commit()
        print(f'{data_name} successfully created!')
    except Exception as error:
        print(f'Error creating {data_name}: {str(error)}')
    finally:
        connection.close()

if __name__ == "__main__":
    schema_sql = "CREATE SCHEMA 143Designs"

    user_table_sql = '''
        CREATE TABLE 143Designs.User(
            user_id SERIAL PRIMARY KEY,
            email VARCHAR(60) UNIQUE NOT NULL,
            passwrd VARCHAR(60) NOT NULL
        );
    '''

    test_user_1_sql = "INSERT INTO 143Designs.User (user_id, email, passwrd) VALUES (-1, 'test@email.com', 'test');"

    test_user_2_sql = "INSERT INTO 143Designs.User (user_id, email, passwrd) VALUES (-2, " \
                      "'delete-all-sessions@email.com', 'test');"

    session_table_sql = '''
        CREATE TABLE 143Designs.Session (
            session_id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            expiration TIMESTAMP NOT NULL,
            CONSTRAINT user_session_fk FOREIGN KEY (user_id) REFERENCES 143Designs.User(user_id) ON DELETE CASCADE
        );
    '''

    test_session_1_sql = f"INSERT INTO 143Designs.Session (session_id, user_id, expiration) VALUES (-1, -1, " \
                         f"{datetime.now() - timedelta(minutes=15)});"

    request_table_sql = '''
        CREATE TABLE 143Designs.Request (
            request_id SERIAL PRIMARY KEY,
            first_name VARCHAR(36) NOT NULL,
            last_name VARCHAR(36) NOT NULL,
            email VARCHAR(60) NOT NULL,
            phone_number VARCHAR(15),
            message TEXT NOT NULL,
            complete BOOLEAN NOT NULL,
            timestamp TIMESTAMP NOT NULL
        );
    '''

    review_table_sql = '''
        CREATE TABLE 143Designs.Review (
            review_id SERIAL PRIMARY KEY,
            first_name VARCHAR(36) NOT NULL,
            last_name VARCHAR(36) NOT NULL,
            text TEXT NOT NULL,
            rating DECIMAL(1, 1) NOT NULL
        );
    '''

    work_table_sql = '''
        CREATE TABLE 143Designs.Work (
            work_id SERIAL PRIMARY KEY,
            first_name VARCHAR(36) NOT NULL,
            last_name VARCHAR(36) NOT NULL,
            description TEXT NOT NULL
        );
    '''

    create_data(schema_sql, "Database schema")
    create_data(user_table_sql, "User table")
    create_data(test_user_1_sql, "Test user 1")
    create_data(test_user_2_sql, "Test user 2")
    create_data(session_table_sql, "Session table")
    create_data(test_session_1_sql, "Test session 1")
    create_data(request_table_sql, "Request table")
    create_data(review_table_sql, "Review table")
    create_data(work_table_sql, "Work table")

    print("Database setup successfully!")
