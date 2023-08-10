from sqlite3 import connect, Cursor, Connection
import json

class UserRepository:
    def __init__(self, db_connection, db_cursor = None):
        self.connection = db_connection
        self.cursor = db_cursor if db_cursor else db_connection.cursor()

    def get_all_users(self):
        for user in self.cursor.execute("SELECT * FROM Users"):
            yield user

    def get_users_by_name(self, name):
        for user in self.cursor.execute("SELECT * FROM Users WHERE name = ?",(name,)):
            yield user


# repository

#DTOs
class SeedDataFileDto:
    def __init__(self, users):
        self.users = [(user['name'],user['job'],user['pay']) for user in users]



def create_connection():
    try:
        return connect("user.db")
    except Exception as e:
        print(f"Exception {e}")


def seed_data(connection: Connection, cursor: Cursor):
    with open("Data.json", "r") as data_file:
        json_data = json.load(data_file)
        seed_data = SeedDataFileDto(**json_data)
        cursor.executemany("INSERT INTO users VALUES(?, ?, ?)", seed_data.users)

        # INSERT runs through a transaction implicitly
        connection.commit()

def setup_db(connection: Connection, cursor: Cursor):
    # ensures that the db is set up properly in terms of tables
    try:
        # check to see if the table already exists and is seeded
        user_table = cursor.execute("SELECT name FROM sqlite_master WHERE name='Users'")
        # see if db exists
        if user_table.fetchone() is not None:
            tommy = cursor.execute("SELECT * from Users where name='Tommy'")
            # see if data is seeded
            tommy_data = tommy.fetchone()
            if tommy_data is not None:
                return
            else:
                # re-seed data if everything else exists
                seed_data(connection, cursor)
        else:
            cursor.execute("CREATE TABLE users(name,job,pay)")

            seed_data(connection, cursor)
    except Exception as e:
        print(f"Exception setting up db {e}")



if __name__ == "__main__":
    # connect to db, create file if dne
    with create_connection() as connection:
        # creates a db cursor to execute queries
        cursor = connection.cursor()

        # first time setup, does nothing after
        setup_db(connection, cursor)

        user_repository = UserRepository(connection, cursor)

        print("Get all users")
        for user in user_repository.get_all_users():
            print(user)

        print("Get users by name")
        for user in user_repository.get_users_by_name("Tommy"):
            print(user)





