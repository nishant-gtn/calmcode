# Python Development Guide

## Code Formatting

### Black

To format a Python file using `black`, run:

```bash
black filename.py
```

**Example:** If you have a Python file `example.py` with inconsistent formatting, running `black example.py` will reformat it according to PEP 8 standards.

### Flake8

To check a Python file for style guide enforcement using `flake8`, run:

```bash
flake8 filename.py
```

**Example:** Running `flake8 example.py` will highlight style issues like missing docstrings or line length violations.

## Pre-commit Hooks

### Sample Configuration

To generate a sample pre-commit configuration file:

```bash
pre-commit sample-config | out-file .pre-commit-config.yaml -encoding utf8
```

**Example:** This command creates a `.pre-commit-config.yaml` file with default configurations that you can customize.

### Install Pre-commit

To install the pre-commit hooks:

```bash
pre-commit install
```

**Example:** This command installs hooks defined in your `.pre-commit-config.yaml` file to ensure code quality checks run before each commit.

### Update Pre-commit Hooks

To update the hooks to their latest versions:

```bash
pre-commit autoupdate
```

**Example:** This command updates the versions of pre-commit hooks specified in `.pre-commit-config.yaml`.

## Performance Profiling

### PyInstrument

To profile a Python script or folder using `pyinstrument`, run:

```bash
pyinstrument folder/script.py
```

**Example:** This command profiles the `script.py` file, showing where time is spent during execution.

### Generate HTML Report

To generate an HTML report:

```bash
pyinstrument -r html path/script.py
```

**Example:** This command produces an HTML report that you can view in a web browser to analyze performance data.

### Generate Speedscope Report

To generate a Speedscope report and visualize it:

```bash
pyinstrument -r speedscope -o speedscope.json path/script.py
```

**Example:** This command creates a `speedscope.json` file which you can visualize using [Speedscope](https://www.speedscope.app/) to get a detailed performance breakdown.

## Testing

### Running Tests with Pytest

To run tests with `pytest`:

```bash
pytest
```

**Example:** Running `pytest` in a directory will automatically find and execute tests in files matching the pattern `test*.py`.

### Running a Specific Test

To run a specific test function in a file:

```bash
pytest file.py::function
```

**Example:** Running `pytest test_example.py::test_function` will execute only the `test_function` within `test_example.py`.

### Verbose Output

To get verbose output from `pytest`:

```bash
pytest --verbose
```

**Example:** This command provides detailed information about each test, including passed, failed, and skipped tests.

### Setting Up Packages

After creating packages and folders:

```bash
python setup.py develop
```

**Example:** This command installs your package in "development mode," allowing you to test changes without reinstalling the package.

## Code Coverage

### Installing Coverage Plugin

To install the coverage plugin:

```bash
python -m pip install pytest-cov
```

**Example:** This command installs the `pytest-cov` plugin to measure code coverage during testing.

### Running Tests with Coverage

To run tests and generate a coverage report:

```bash
pytest --cov packagename
```

**Example:** This command runs tests for `packagename` and reports the coverage percentage.

### Generating an HTML Coverage Report

To generate an HTML coverage report:

```bash
pytest --cov packagename --cov-report html
```

**Example:** This command creates an HTML report in the `htmlcov` directory, which you can view in a browser to see which parts of your code are covered by tests.

## Pytest Advanced Usage

### Running Tests with Markers

To run only tests marked with a certain marker:

```bash
pytest file.py -m `mark`
```

**Example:** Running `pytest test_example.py -m slow` will execute only the tests marked with the `@pytest.mark.slow` decorator.

### Parallel Test Execution

To run tests in parallel using `xdist`:

```bash
pytest -n 2     # use 2 cores
pytest -n auto  # use all available cores
```

**Example:** This command speeds up testing by distributing tests across multiple CPU cores.

### Stopping on First Error

To stop `pytest` when an error is found:

```bash
pytest -x
```

**Example:** This command halts the test suite as soon as the first test failure occurs, which can save time during debugging.

### Verbose Output with Clarity

After installing the `clarity` plugin, you can run:

```bash
pytest -x -vv
```

**Example:** This command combines verbose output with the `-x` option to stop on the first error, providing detailed information about the error.

## Security

### Bandit (Security Analysis)

To check a Python file for security issues using `Bandit`:

```bash
bandit file.py
```

**Example:** Running `bandit example.py` will analyze the file for common security vulnerabilities.

### Checking All Files in a Folder

To check all files within a folder:

```bash
bandit -r folder/
```

**Example:** This command scans all Python files in `folder/` for security issues.

### Skipping Lines from Security Checks

To skip checking a specific line, add `# nosec` to the concerned line.

**Example:**

```python
# Some insecure code # nosec
```

The `# nosec` comment tells Bandit to ignore security concerns for that line.

# MkDocs

## Installation

To install MkDocs, use the following command:

```bash
pip install mkdocs
```

## Creating a New Project

To create a new MkDocs project in the current directory, run:

```bash
mkdocs new .
```

**Example:** After running this command, you will see a directory structure like:

```
.
├── docs
│   └── index.md
└── mkdocs.yml
```

## Serving the Documentation Locally

To serve the documentation locally and view it in your browser:

```bash
mkdocs serve
```

**Example:** After serving, your documentation will be available at `http://127.0.0.1:8000/`.

## Customizing CSS

To apply custom CSS, add the `extra_css` configuration in `mkdocs.yml`:

```yaml
extra_css:
  - custom.css
```

**Example:** If `custom.css` contains styles to change the background color, those styles will be applied to the site.

## Changing the Theme

To change the theme of your MkDocs site, modify the `theme` section in `mkdocs.yml`:

```yaml
theme:
  name: readthedocs
```

**Example:** The `readthedocs` theme will give your site a clean, professional look similar to the Read the Docs website.

## Using MkDocs Material Theme

To install the MkDocs Material theme, use:

```bash
pip install mkdocs-material
```

To apply the Material theme and customize it, modify `mkdocs.yml`:

```yaml
theme:
  name: "material"
  palette:
    primary: "purple"
    accent: "cyan"
  font:
    text: "Ubuntu"
  logo:
    icon: "cloud"
```

**Example:** This configuration sets the primary color to purple, the accent color to cyan, uses the Ubuntu font, and includes a cloud icon as the logo.

## Adding Markdown Extensions

To add Markdown extensions, include the following in your `mkdocs.yml`:

```yaml
markdown_extensions:
  - footnotes
  - codehilite:
      linenums: true
```

**Example:** The `footnotes` extension allows you to add footnotes like this[^1], and `codehilite` adds line numbers to code blocks.

## Adding Extras (Emojis, Custom Checkbox, Expressions)

To add features like emojis, custom checkboxes, and math expressions, install the `pymdown-extensions` package:

```bash
pip install pymdown-extensions
```

Add the following to `mkdocs.yml` to enable these features:

```yaml
markdown_extensions:
  - pymdownx.arithmatex
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.emoji:
      emoji_generator: !!python/name:pymdownx.emoji.to_svg
  - footnotes
  - codehilite:
      linenums: true
```

**Example:**

- `arithmatex` enables LaTeX-style math expressions.
- `tasklist` provides custom checkboxes for task lists.
- `emoji` adds support for emojis like :smile:.

Here is how you might use these in a Markdown file (`backend.md`):

### `backend.md` Example:

````markdown
# Backend

Our backend is written in Python.
We use some JavaScript here and there.

![Backend Image](/images/backend.png)

This image[^1] demonstrates something interesting.

```python
for i in range(10):
    print(i)
```
````

### Demo :smile:

## Roadmap

- [x] Wake up
- [x] Have coffee
- [ ] Work

## Maths

I can do some maths $a + b < c$ inline.

$$ a + c^2 < b^7 $$

[^1]: From a PyData video, can be found [here](https://www.youtube.com/watch?v=Z8MEFI7ZJlA&t=943s).

```
In this example:
- The emoji `:smile:` will be rendered as a smiley face.
- The roadmap section uses custom checkboxes, where the first two tasks are completed.
- The math expressions demonstrate inline and block-level mathematical notation.

```

# Logging in Python

Logging is crucial for monitoring and debugging our applications. Here’s how we can set up and use logging effectively in Python.

## Basic Logging Setup

We start with a basic logging configuration that sends logs to the console.

```python
import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
fmt = '%(levelname)s %(asctime)s %(filename)s %(funcName)s %(lineno)d %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.setLevel(logging.WARNING)
```

### Configuration Details

- **Handler**: `StreamHandler()` directs logs to the console.
- **Formatter**: Defines the log message format with level, timestamp, filename, function name, line number, and message.
- **Log Level**: Set to `WARNING`, so only `WARNING`, `ERROR`, and `CRITICAL` messages are logged.

This setup ensures we see significant issues and errors in the console output.

## Log Levels

To capture different levels of log messages, we adjust the logging level and include various log statements.

```python
logger.debug('This is a debug statement')
logger.info('This is an info statement')
logger.warning('This is a warning statement')
logger.error('This is an error statement')
logger.critical('This is a critical statement')
```

### Changes

- **Log Level**: Adjusting levels like `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL` allows us to control which messages are logged.
- **Log Messages**: Different log statements demonstrate how each level is captured based on the set log level.

With `WARNING` set as the level, only `WARNING`, `ERROR`, and `CRITICAL` messages appear.

## Logging to a File

We can extend our logging configuration to also write messages to a file for persistent storage.

```python
file_handler = logging.FileHandler("debug.log")
file_handler.setLevel(logging.DEBUG)
fmt_file = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
file_formatter = logging.Formatter(fmt_file)
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
```

### Changes

- **Handler**: Added `FileHandler()` to log messages to a file (`debug.log`).
- **Log Levels**: Different levels for console and file logging, allowing detailed file logs and cleaner console output.
- **Formatter**: Custom format for file logs.

This setup enables detailed file logging while keeping console output more concise.

## Handling Errors

To capture errors with traceback, we enhance our logging setup.

```python
import sys

from logger import logger  # Assuming logger is configured as above

if __name__ == "__main__":
    logger.debug("Program started.")
    try:
        ticker = sys.argv[1]
        logger.info(f"Will find summary for {ticker}.")
        print(f"The average stock price is {summary(ticker)}")
        logger.debug("Program ended with success.")
    except BaseException:
        logger.error("Error happened!", exc_info=True)
```

### Changes

- **Exception Logging**: Added `exc_info=True` to log traceback details when an error occurs.

This helps us diagnose issues by showing where and why an error happened.

## Using Rich for Enhanced Logging

`Rich` provides colorful and formatted logging output to enhance readability.

```python
from rich.logging import RichHandler

shell_handler = RichHandler()
shell_handler.setLevel(logging.DEBUG)
fmt_shell = '%(message)s'
shell_formatter = logging.Formatter(fmt_shell)
shell_handler.setFormatter(shell_formatter)

logger.addHandler(shell_handler)
```

### Changes

- **Handler**: Replaced `StreamHandler()` with `RichHandler()` for enhanced console output.
- **Formatter**: Simplified format for rich console logs while retaining detailed file logs.

`Rich` makes console logs more readable and visually appealing, while file logs retain detailed information for reference.
