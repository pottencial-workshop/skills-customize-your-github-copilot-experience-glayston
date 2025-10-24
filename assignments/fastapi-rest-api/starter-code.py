"""
Starter code for FastAPI REST API assignment
Building a Books API with CRUD operations

TODO: Complete the implementation following the assignment requirements
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Books API", version="1.0.0")

# TODO: Define the Book model using Pydantic BaseModel
# Include fields: id (int), title (str), author (str), year (int), genre (str)
class Book(BaseModel):
    pass


# In-memory storage for books (for simplicity)
books_db = []


# TODO: Implement GET endpoint to retrieve all books
# Endpoint: GET /books
@app.get("/books")
def get_books():
    pass


# TODO: Implement GET endpoint to retrieve a single book by ID
# Endpoint: GET /books/{book_id}
@app.get("/books/{book_id}")
def get_book(book_id: int):
    pass


# TODO: Implement POST endpoint to create a new book
# Endpoint: POST /books
@app.post("/books", status_code=201)
def create_book(book: Book):
    pass


# TODO: Implement PUT endpoint to update an existing book
# Endpoint: PUT /books/{book_id}
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    pass


# TODO: Implement DELETE endpoint to remove a book
# Endpoint: DELETE /books/{book_id}
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    pass


# BONUS: Add query parameters for filtering (Task 2)
# Modify the get_books endpoint to accept optional query parameters:
# - author: str
# - genre: str
# - min_year: int
# - max_year: int


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
