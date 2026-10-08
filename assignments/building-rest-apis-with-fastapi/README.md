# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework. Students will create endpoints, define data models, and return structured JSON responses for a small application.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App

#### Description
Create a basic FastAPI application and confirm that it serves a simple JSON response from the root endpoint.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Define a root endpoint using `@app.get("/")`
- Return a JSON response such as a welcome message
- Run the app locally and verify the endpoint responds successfully

### 🛠️ Build CRUD-style Endpoints

#### Description
Create a small API for managing a list of items, such as tasks, books, or products, using FastAPI route handlers and request models.

#### Requirements
Completed program should:

- Define a data model using `BaseModel`
- Create endpoints to list items and add a new item
- Add an endpoint to retrieve a single item by ID
- Return JSON data in a consistent structure
- Handle missing items with an appropriate HTTP error response

### 🛠️ Add Validation and Documentation

#### Description
Improve the API by adding basic validation and using FastAPI features that make the API easier to understand and test.

#### Requirements
Completed program should:

- Validate required fields and values in request payloads
- Use meaningful response status codes for creation and missing resources
- Include a description or clear naming for each endpoint
- Confirm that the automatically generated API docs can be opened in the browser
