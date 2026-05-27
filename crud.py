from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

books_db = [
    {
        "id" : 1,
        "title" : "Python",
        "author" : "John",
        "isbn" : "1234567890",
        "price" : 29.99
    },
    {
        "id" : 2,
        "title" : "Java",
        "author" : "Doe",
        "isbn" : "1234567891",
        "price" : 39.99
    },
    {
        "id" : 3,
        "title" : "C++",
        "author" : "Smith",
        "isbn" : "1234567892",
        "price" : 49.99
    },
    {
        "id" : 4,
        "title" : "React",
        "author" : "John",
        "isbn" : "1234567890",
        "price" : 29.99
    }
]

app = FastAPI()

class Book(BaseModel):
    id : int
    title : str
    author : str
    isbn : str
    price : float

@app.get("/books")
def get_all_books():
    return books_db

@app.post("/create")
def create_book(book : Book):
    new_book = book.model_dump()
    books_db.append(new_book)
    return new_book

@app.get('/book')
def get_book(id:int):
    for book in books_db:
        if book['id'] == id:  
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
@app.put('/update/{id}')
def update_book(id:int, book:Book):
    for db_book in books_db:
        if db_book['id'] == id:  
            db_book['title'] = book.title
            db_book['author'] = book.author
            db_book['isbn'] = book.isbn
            db_book['price'] = book.price
            return db_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete('/delete/{id}')
def delete_book(id:int):
    for db_book in books_db:
        if db_book['id'] == id:  
            books_db.remove(db_book)
            return {'message' : f'{db_book['title']} book deleted successfully'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")