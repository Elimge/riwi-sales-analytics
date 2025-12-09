import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_engine():
    """
    Creates and returns a SQLAlchemy engine for the PostgreSQL database.
    """
    try:
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")

        # Construct the connection url
        db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        
        # Create engine
        engine = create_engine(db_url)
        print(f"Successfully created engine for database: {db_name}")
        return engine
    except Exception as e:
        print(f"Error creating database engine: {e}")
        return None

def test_connection():
    """
    Simple function to test if the connection works.
    """
    engine = get_db_engine()
    if engine:
        try:
            with engine.connect():
                print("Connection successful!")
        except Exception as e:
            print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_connection()