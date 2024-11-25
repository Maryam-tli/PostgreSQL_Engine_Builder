from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the connection string
connection_string = "postgresql+psycopg2://your_username:your_password@localhost:5432/your_database"

# Create the database engine, a base class, Set up a session factory and Create a session instance
engine = create_engine(connection_string)
Base = declarative_base()
meeting = sessionmaker(bind=engine)
session = meeting()


# Define the Person class to represent the 'human' table in the database
class Person(Base):
    __tablename__ = "human"
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=True)

    # Define a string representation method
    def __repr__(self):
        return f"our human info is {self.id},{self.full_name},{self.age},{self.email}"


# Create all tables defined by the ORM models
Base.metadata.create_all(engine)
