# Terminal Spinner Package

A simple Python package to display a spinner in the center of the terminal screen.

## Features

- Displays a rotating spinner in the center of the terminal regardless the size of the screen.
- Clears the screen before starting the spinner.
- Hides the cursor while the spinner is running.
- Restores the cursor to its original position after completion and clears the screen again.

## Installation

You can install the package via pip (to be updated once the package is published to PyPI):

```sh
pip install terminal-spinner
```

## How to use

```python
from terminal_spinner import run_spinner

# Run the spinner for X seconds, 5 by default
run_spinner(duration=5)
```

### Example

```python
# example.py

from terminal_spinner import run_spinner

def main():
    print("Starting spinner...")
    run_spinner(duration=3)
    print("Spinner done!")

if __name__ == "__main__":
    main()
```

```sh
python example.py
```

## License

This project is licensed under the MIT License

## Links

- [GitHub repository](https://github.com/ASanchz85/spinner_shell_python)
- [Pypi repository](https://pypi.org/project/terminal-spinner/)
