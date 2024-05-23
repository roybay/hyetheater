import sys
import os
from api.orm import connect_db

# Add the project root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))  # noqa E501

connect_db()  # Ensure the database mapping is generated before tests
