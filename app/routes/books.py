from sqlalchemy.orm import Session
from sqlalchemy import select

from fastapi.responses import FileResponse, JSONResponse

from app.models_database import Books
from database import engine
from config import app

@app.get("/")
def main_page():
    return FileResponse("templates/index.html")


@app.get("/books")
def send_books(page: int = 1, limit: int = 10):
    with Session(engine) as session:
        # Получаем общее количество книг для пагинации
        total_books = session.query(Books).count()
        
        # Вычисляем книги для текущей страницы
        books = session.execute(
            select(Books).offset((page - 1) * limit).limit(limit)
        ).scalars().all()
        
        # Возвращаем книги и общее количество в JSON
        return JSONResponse(content={"totalBooks": total_books, "books": books})

@app.get("/books/search")
def search_book():
    pass

@app.get("/books/add")
def add_books_page():
    return FileResponse("templates/add_books.html")