# Introduction to FastAPI

## 🚀 What is FastAPI?

**FastAPI** is a modern Python web framework built specifically for creating **APIs** (RESTful services). It’s designed to be:

- **Fast**: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
- **Easy to Use**: With intuitive syntax and automatic docs.
- **Automatic validation**: Based on Python type hints.
- **Built-in API Docs**: Swagger UI and ReDoc out of the box.
- **Asynchronous**: Fully supports `async` and `await`.

---

## 📦 Key Features

| Feature | Description |
|--------|-------------|
| 🔧 Type Hints | Uses standard Python type hints for input/output validation |
| 🧪 Auto Validation | Ensures request data is correct before hitting your logic |
| 📃 OpenAPI & Swagger | Auto-generates documentation |
| ⚡ Async Support | Built on `Starlette`, supports asynchronous code |
| 🛡️ Security | OAuth2, JWT, basic auth, etc., supported out of the box |

---

## 🛠 Basic Example

Here's a simple FastAPI app:

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

To run it:

```bash
uvicorn main:app --reload
```

Access the docs:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧬 Request Models with Pydantic

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

FastAPI will automatically:
- Validate input data
- Generate API docs
- Convert JSON payloads to Python objects

---

## 🧵 Async Support

```python
@app.get("/wait")
async def wait():
    await some_async_function()
    return {"status": "done"}
```

You can use `async` endpoints easily, ideal for I/O-heavy tasks.

---

## 📄 Summary

FastAPI is great if you’re looking for:
- Fast development speed
- Built-in validation and docs
- Modern Pythonic syntax
- Production-grade performance