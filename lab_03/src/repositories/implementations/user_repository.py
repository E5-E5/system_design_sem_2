
from src.model.user import User

from src.repositories.implementations.database import Database
from src.repositories.interfaces.user_repository import (
    IUserRepository
)


class UserRepository(IUserRepository):

    def __init__(self):

        self.db = Database()

    def create_user(self, user: User):

        connection = self.db.get_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO users (
            login,
            password,
            first_name,
            last_name
        )
        VALUES (%s, %s, %s, %s)
        RETURNING id;
        """

        cursor.execute(
            query,
            (
                user.login,
                user.password,
                user.first_name,
                user.last_name
            )
        )

        user_id = cursor.fetchone()[0]

        connection.commit()

        cursor.close()

        return user_id

    def get_by_login(self, login: str):

        connection = self.db.get_connection()

        cursor = connection.cursor()

        query = """
        SELECT
            id,
            login,
            password,
            first_name,
            last_name
        FROM users
        WHERE login = %s;
        """

        cursor.execute(query, (login,))

        row = cursor.fetchone()

        cursor.close()

        if row is None:
            return None

        return User(
            id=row[0],
            login=row[1],
            password=row[2],
            first_name=row[3],
            last_name=row[4]
        )