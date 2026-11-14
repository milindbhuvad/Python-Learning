from day_8_database import get_db_connection

try:
    connection = get_db_connection()

    if connection.is_connected():
        print("Connection to the database was successful.")

    connection.close()
except Exception as error:
    print("Database connection failed:", error)