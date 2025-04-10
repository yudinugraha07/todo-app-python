# Todo App in Python

## Overview
This is a simple command-line-based Todo application built using Python. The app allows users to manage their tasks effectively by adding, viewing, updating, and deleting tasks.

## Features
- Add new tasks with descriptions and due dates.
- View all tasks in a structured format.
- Mark tasks as completed.
- Delete tasks.
- Save tasks persistently using a file-based storage system.

## Requirements
- Basic knowledge of Python programming.
- Familiarity with RESTful APIs and HTTP methods.
- A text editor or IDE (such as Visual Studio Code).
- Python 3.11

## Technologies Used
- FastAPI (https://fastapi.tiangolo.com/). Read Introduction to FastAPI [here](./docs/introduction-to-fastapi.md)
- Uvicorn (for serving the FastAPI application)
- SQLite (or any other relational database if you want to make it more advanced).

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yudinugraha07/todo-app-python.git
    ```
2. Navigate to the project directory:
    ```bash
    cd todo-app-python
    ```
3. Create Virtual Environment and Activate it:
   ```bash
   python -m venv venv          # create a virtual environment
   source venv/bin/activate     # activate the virtual environment
   # deactivate virtual environment with this command: deactivate
   ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn app:app --reload
   ```
   - The `--reload` flag enables auto-reloading for development purposes.
2. The application will be available at `http://127.0.0.1:8000`.

## Testing the Application

1. Open your browser or a tool like [Postman](https://www.postman.com/) or [cURL](https://curl.se/).
2. Use the following endpoints to interact with the application:

   - **GET `/`**: Check the welcome message.
   - **GET `/todos`**: Retrieve all TODO items.
   - **GET `/todos/{todo_id}`**: Retrieve a specific TODO item by its ID.
   - **POST `/todos`**: Create a new TODO item. Example JSON body:
     ```json
     {
       "id": 1,
       "title": "Sample TODO",
       "description": "This is a sample TODO item",
       "completed": false
     }
     ```
   - **PUT `/todos/{todo_id}`**: Update an existing TODO item. Example JSON body:
     ```json
     {
       "id": 1,
       "title": "Updated TODO",
       "description": "This TODO item has been updated",
       "completed": true
     }
     ```
   - **DELETE `/todos/{todo_id}`**: Delete a TODO item by its ID.

3. Access the automatically generated API documentation:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Notes

- The application uses an in-memory database, so all data will be lost when the server restarts.
- For production, consider using a persistent database and deploying the app using a production-grade server.

## File Structure
```
todo-app-python/
├── todo_app.py         # Main application file
├── tasks.json          # File for storing tasks persistently
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (if applicable)
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.