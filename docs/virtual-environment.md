# Setting Up a Virtual Environment

## Overview

A virtual environment is an isolated environment for Python projects. It allows you to manage dependencies for a specific project without affecting the global Python installation or other projects. This ensures that each project has its own set of libraries and versions, making it easier to maintain and avoid conflicts.

## Create a Virtual Environment

Follow these steps to create a virtual environment for your Python project:

1. **Navigate to the Project Directory**  
    Open a terminal and navigate to the project directory:  
    ```bash
    cd /todo_app_python
    ```

2. **Create the Virtual Environment**  
    Run the following command to create a virtual environment named `venv`:  
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**  
    - On macOS/Linux:  
      ```bash
      source venv/bin/activate
      ```
    - On Windows:  
      ```bash
      venv\Scripts\activate
      ```

4. **Install Dependencies**  
    After activation, install the required dependencies (if any):  
    ```bash
    pip install -r requirements.txt
    ```

5. **Deactivate the Virtual Environment**  
    When done, deactivate the virtual environment:  
    ```bash
    deactivate
    ```
