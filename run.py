
from app.models_database import Base, Books
from database import engine
from config import app

from app.routes.books import *


Base.metadata.create_all(engine)