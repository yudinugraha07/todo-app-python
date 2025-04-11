# Python for C# Developers

### **1. Basic Syntax Differences**

| Concept              | C#                                  | Python                          |
|----------------------|--------------------------------------|----------------------------------|
| Variable Declaration | `int x = 5;`                         | `x = 5`                         |
| Block Scope          | `{ ... }`                            | Indentation                     |
| Semicolons           | Required (`;`)                       | Not used                        |
| Print                | `Console.WriteLine("Hello");`       | `print("Hello")`                |
| String Interpolation | `$"Hello {name}"`                   | `f"Hello {name}"`               |

---

### **2. Data Types**

Python is dynamically typed:

```python
x = 10              # int
name = "Alhaq"      # string
price = 19.99       # float
is_valid = True     # bool
```

**Collections:**

```python
my_list = [1, 2, 3]         # Like List<int>
my_dict = {'a': 1, 'b': 2}  # Like Dictionary<string, int>
my_set = {1, 2, 3}          # Like HashSet<int>
```

---

### **3. Functions and Classes**

```python
def greet(name):
    return f"Hello, {name}"

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hi, I'm {self.name}")
```

Equivalent to:

```csharp
public class Person {
    public string Name { get; set; }

    public Person(string name) {
        Name = name;
    }

    public void SayHello() {
        Console.WriteLine($"Hi, I'm {Name}");
    }
}
```

---

### **4. List Comprehensions = LINQ**

```python
squares = [x*x for x in range(10)]
```

Like:

```csharp
var squares = Enumerable.Range(0, 10).Select(x => x * x);
```

---

### **5. Async/Await**

```python
import asyncio

async def main():
    await asyncio.sleep(1)
    print("Done")

asyncio.run(main())
```

Roughly equivalent to:

```csharp
await Task.Delay(1000);
Console.WriteLine("Done");
```

---

### **6. File Handling**

```python
with open('file.txt', 'r') as f:
    contents = f.read()
```

Like:

```csharp
using (var reader = new StreamReader("file.txt"))
{
    var contents = reader.ReadToEnd();
}
```

---

### **7. Working with JSON**

```python
import json

data = json.loads('{"name": "Alhaq"}')
json_str = json.dumps(data)
```

Equivalent to:

```csharp
var data = JsonSerializer.Deserialize<Dictionary<string, string>>(json);
var jsonStr = JsonSerializer.Serialize(data);
```

---

### **8. Packages and Virtual Environments**

- Like NuGet, Python uses **pip** (or **Poetry** for more structure).
- Use `venv` to create isolated environments:
  
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install requests
```

---

### **9. Popular Libraries (Back-End Focus)**

- **FastAPI** or **Flask** → Similar to ASP.NET Minimal APIs
- **SQLAlchemy / Tortoise ORM** → Like Entity Framework
- **Requests** → Like `HttpClient`
- **Pytest** → Like xUnit/NUnit

---

### **10. Practical Practice Idea**

Build a small REST API with FastAPI — like a To-Do List or Notes App — using:
- FastAPI (backend)
- PostgreSQL or SQLite
- ORM (SQLAlchemy)
- Async handling

---