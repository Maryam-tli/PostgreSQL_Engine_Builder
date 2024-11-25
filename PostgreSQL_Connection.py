from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the connection string
connection_string = "postgresql+psycopg2://your_username:your_password@localhost:5432/your_database"

# Create the database engine, a base class, Set up a session factory and Create a session instance
motor = create_engine(connection_string)
Base = declarative_base()
meeting = sessionmaker(bind=motor)
session = meeting()
