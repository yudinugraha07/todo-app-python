# Setting Up Alias for Python3 and Pip3 in Zsh

Follow these steps to set up aliases for `python3` to `python` and `pip3` to `pip` in your Zsh terminal:

## 1. Open the Zsh Configuration File
Edit the `.zshrc` file located in your home directory:
```bash
nano ~/.zshrc
```

## 2. Add the Aliases
Add the following lines to the end of the file:
```bash
alias python='python3'
alias pip='pip3'
```

## 3. Save and Exit
Save the changes and exit the editor. If using `nano`, press `CTRL + O`, then `Enter`, and `CTRL + X`.

## 4. Apply the Changes
Reload the `.zshrc` file to apply the changes:
```bash
source ~/.zshrc
```

## 5. Verify the Aliases
Run the following commands to confirm the aliases are set up correctly:
```bash
python --version
pip --version
```

You should see the versions of `python3` and `pip3` displayed.

## Notes
- Ensure `python3` and `pip3` are installed on your system.
- If you encounter issues, check your `.zshrc` file for typos.

That's it! You now have `python` and `pip` pointing to `python3` and `pip3` respectively.