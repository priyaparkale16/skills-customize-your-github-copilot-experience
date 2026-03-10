# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will create a REST API service using FastAPI, learning request handling, routing, validation, and response serialization for backend web applications.

## 📝 Tasks

### 🛠️ Task 1: Create basic FastAPI endpoints

#### Description
Build a Python FastAPI app with a set of REST endpoints for a simple resource (e.g., tasks, notes, or products).

#### Requirements
Completed program should:

- Create a FastAPI app instance in `main.py` or `starter-code.py`
- Implement CRUD endpoints for the resource:
  - `GET /items` to list items
  - `GET /items/{item_id}` to fetch an item by ID
  - `POST /items` to create an item
  - `PUT /items/{item_id}` to update an item
  - `DELETE /items/{item_id}` to delete an item
- Use Pydantic models for request and response validation
- Return JSON responses with appropriate HTTP status codes

### 🛠️ Task 2: Add query filters and error handling

#### Description
Extend the API with query parameters, path validation, and proper HTTP error handling.

#### Requirements
Completed program should:

- Support filtering returned items by a query parameter (e.g., `?completed=true`)
- Validate path parameters and return `HTTP 404` when an item is not found
- Use `HTTPException` for invalid operations (e.g., duplicate IDs or invalid input)
- Include clear success and error messages in JSON responses

## 📦 Starter Code

A starter file is included at `starter-code.py` to launch the FastAPI app.
