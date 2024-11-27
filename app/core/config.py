from decouple import config

DATABASE_FILE = config("DATABASE_FILE", default="books.db")
