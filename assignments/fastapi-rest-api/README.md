# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Learn to build modern, fast REST APIs using FastAPI framework. You'll create endpoints, handle HTTP methods, validate data, and implement CRUD operations for a simple resource management system.

## 📝 Tarefas

### 🛠️	Create a Books API

#### Description
Build a RESTful API to manage a collection of books. The API should support creating, reading, updating, and deleting book records. Implement proper HTTP methods, status codes, and data validation using FastAPI's built-in features.

#### Requirements
Completed program should:

- Define a Book model with fields: id, title, author, year, and genre
- Implement GET endpoint to retrieve all books
- Implement GET endpoint to retrieve a single book by ID
- Implement POST endpoint to create a new book with data validation
- Implement PUT endpoint to update an existing book
- Implement DELETE endpoint to remove a book by ID
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include automatic API documentation at `/docs` endpoint


### 🛠️	Add Query Parameters and Filtering

#### Description
Enhance your Books API by adding query parameters to filter and search through the book collection. Implement optional filters that allow users to search by author, genre, or year range.

#### Requirements
Completed program should:

- Add query parameters to the GET all books endpoint (author, genre, min_year, max_year)
- Filter results based on provided query parameters
- Support multiple filters simultaneously
- Return empty list when no books match the criteria
- Maintain backward compatibility (endpoint works without query parameters)
