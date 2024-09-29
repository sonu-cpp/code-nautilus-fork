# code-nautilus-fork
# Changes and Improvements from the original extension
1. Removed shell=True in subprocess execution

    Reason: Avoids potential command injection risks by directly passing arguments without invoking a shell.
    Impact: Increased security by preventing malicious shell commands from being injected into the script.

2. Replaced subprocess.call() with subprocess.run()

    Reason: subprocess.run() provides more control and is the preferred method in Python 3 for executing system commands.
    Impact: Improved clarity and safer execution of subprocesses.

3. Absolute path handling for files and directories

    Reason: Using os.path.abspath() ensures that all file and directory paths are fully qualified, reducing the chance of unintended behavior with relative paths.
    Impact: Improves security by ensuring that all paths are valid and absolute.

4. Full path for VSCode executable

    Reason: Ensures that the correct VSCode executable is used. You can modify the path if VSCode is installed in a custom location.
    Impact: Prevents the script from accidentally launching the wrong program.

To install, run the following command:

```bash
wget -qO- https://raw.githubusercontent.com/sonux2005/code-nautilus-fork/master/install.sh | bash
```

To Uninstall, run the following command:
```bash
wget -qO- https://raw.githubusercontent.com/sonux2005/code-nautilus-fork/master/uninstall.sh | bash
```
