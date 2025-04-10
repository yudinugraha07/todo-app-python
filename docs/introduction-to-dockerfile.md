# Introduction to Dockerfile

### 🐳 What is a Dockerfile?

A `Dockerfile` is a **text file** that contains a set of **instructions** for building a Docker image. It defines what goes into the image, including:

- Base image (e.g., Python, Node)
- Files to include
- Commands to run (e.g., install packages, set env vars)
- The default command to run when a container starts

---

### 📦 Basic Structure of a Dockerfile

Here's a **simple Dockerfile** for a Python app:

```dockerfile
# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your app code into the container
COPY . .

# 6. Define environment variable (optional)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 7. Set the default command to run the app
CMD ["python", "main.py"]
```

---

### 🔧 Common Instructions

| Instruction | Description |
|-------------|-------------|
| `FROM`      | Sets the base image |
| `WORKDIR`   | Sets the working directory inside the container |
| `COPY`      | Copies files from host to container |
| `RUN`       | Runs commands (like installing packages) during image build |
| `CMD`       | Command to run when the container starts |
| `ENV`       | Sets environment variables |

---

### 🛠 Example Folder Structure

```
myapp/
├── Dockerfile
├── requirements.txt
└── main.py
```

---

### 🚀 Build and Run

1. **Build the Docker image**  
   ```bash
   docker build -t my-python-app .
   ```

2. **Run a container based on the image**  
   ```bash
   docker run -it --rm my-python-app
   ```