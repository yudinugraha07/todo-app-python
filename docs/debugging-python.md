## Debuging in Visual Studio Code

To debug the application in Visual Studio Code, follow these steps:

1. **Install the Python Extension**:
  - Ensure you have the Python extension installed in Visual Studio Code. You can find it in the Extensions Marketplace.

2. **Set Up a Debug Configuration**:
  - Open the `Run and Debug` view by clicking on the play icon in the sidebar or pressing `Ctrl+Shift+D` (Windows/Linux) or `Cmd+Shift+D` (Mac).
  - Click on `create a launch.json file` and select `Python` as the environment.
  - Add the following configuration to the `launch.json` file:
    ```json
    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
        
            {
                "name": "Python Debugger: FastAPI",
                "type": "debugpy",
                "request": "launch",
                "module": "uvicorn",
                "args": [
                    "app:app",
                    "--reload"
                ],
                "jinja": true
            }
        ]
    }
    ```

3. **Set Breakpoints**:
  - Open the file you want to debug and click in the gutter next to the line numbers to set breakpoints.

4. **Start Debugging**:
  - Select the `Python: FastAPI` configuration from the dropdown in the `Run and Debug` view.
  - Click the green play button to start debugging.

5. **Inspect Variables and Execution Flow**:
  - Use the Debug Console to inspect variables and evaluate expressions.
  - Step through the code using the controls in the top bar (Step Over, Step Into, Step Out).

By following these steps, you can debug your FastAPI application effectively in Visual Studio Code.


## Inspect Element Shortcut

- inspect element shortcut for mac: ```cmd+opt+i```

## Environment Variable

- export the env variables to shell env:
    ```bash
    eval $(cat .env | sed 's/^/export /')
    ```
- display the current environment variables and their values
  ```bash
  printenv
  ```
