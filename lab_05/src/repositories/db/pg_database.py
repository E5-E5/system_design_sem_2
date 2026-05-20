import psycopg2


class Database:

    def __init__(self):

        self.connection = psycopg2.connect(
            host="postgres",
            port=5432,
            database="hotel_booking",
            user="postgres",
            password="postgres" #sasha
        )

    def get_connection(self):

        return self.connection