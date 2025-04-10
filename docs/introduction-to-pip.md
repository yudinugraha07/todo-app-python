# Introduction to pip

## 🐍 What is `pip`?

`pip` stands for **"Pip Installs Packages"**. It's the **default package manager for Python**, used to install and manage software packages written in Python. These packages are typically hosted on [PyPI (Python Package Index)](https://pypi.org/).

---

## 🛠️ What Can You Do with `pip`?

| Command | Purpose |
|--------|---------|
| `pip install package_name` | Install a package |
| `pip uninstall package_name` | Remove a package |
| `pip list` | List all installed packages |
| `pip freeze` | Show installed packages in `requirements.txt` format |
| `pip show package_name` | Show package info |
| `pip install -r requirements.txt` | Install all packages listed in a file |

---
## 🔧 Check if pip already Installed
```bash
pip --version
pip3 --version
```

## 🔧 Installing a Package

Example:
```bash
pip install requests
```

This installs the `requests` library so you can do things like HTTP calls in Python.

---

## 📦 Using `requirements.txt`

You can create a file listing all the dependencies for your project:

```bash
pip freeze > requirements.txt
```

And later install them in a new environment:

```bash
pip install -r requirements.txt
```

---

## ✅ Version Management

You can install specific versions:

```bash
pip install fastapi==0.109.0
```

Or upgrade a package:

```bash
pip install --upgrade fastapi
```

---

## ⚙️ Common Options

| Option | Description |
|--------|-------------|
| `--upgrade` | Upgrade the package to the latest version |
| `--user` | Install the package for the current user only |
| `--no-cache-dir` | Don’t use the cache during install |

---

## 💡 Pro Tip

Want to know where a package is installed?

```bash
pip show fastapi
```