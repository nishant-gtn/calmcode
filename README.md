# Python Development Guide

## Code Formatting

### Black

To format a Python file using `black`, run:

```bash
black filename.py
```

### Flake8

To check a Python file for style guide enforcement using `flake8`, run:

```bash
flake8 filename.py
```

## Pre-commit Hooks

### Sample Configuration

To generate a sample pre-commit configuration file:

```bash
pre-commit sample-config | out-file .pre-commit-config.yaml -encoding utf8
```

### Install Pre-commit

To install the pre-commit hooks:

```bash
pre-commit install
```

### Update Pre-commit Hooks

To update the hooks to their latest versions:

```bash
pre-commit autoupdate
```

## Performance Profiling

### PyInstrument

To profile a Python script or folder using `pyinstrument`, run:

```bash
pyinstrument folder/script.py
```

### Generate HTML Report

To generate an HTML report:

```bash
pyinstrument -r html path/script.py
```

### Generate Speedscope Report

To generate a Speedscope report and visualize it:

```bash
pyinstrument -r speedscope -o speedscope.json path/script.py
```

Visualize the output using [Speedscope](https://www.speedscope.app/).

## Testing

### Running Tests with Pytest

To run tests with `pytest`:

```bash
pytest
```

Use test files with names `test*.py` and functions with names `test*()`.

### Running a Specific Test

To run a specific test function in a file:

```bash
pytest file.py::function
```

### Verbose Output

To get verbose output from `pytest`:

```bash
pytest --verbose
```

### Setting Up Packages

After creating packages and folders:

```bash
python setup.py develop
```

## Code Coverage

### Installing Coverage Plugin

To install the coverage plugin:

```bash
python -m pip install pytest-cov
```

### Running Tests with Coverage

To run tests and generate a coverage report:

```bash
pytest --cov packagename
```

### Generating an HTML Coverage Report

To generate an HTML coverage report:

```bash
pytest --cov packagename --cov-report html
```

## Pytest Advanced Usage

### Running Tests with Markers

To run only tests marked with a certain marker:

```bash
pytest file.py -m `mark`
```

### Parallel Test Execution

To run tests in parallel using `xdist`:

```bash
pytest -n 2     # use 2 cores
pytest -n auto  # use all available cores
```

### Stopping on First Error

To stop `pytest` when an error is found:

```bash
pytest -x
```

### Verbose Output with Clarity

After installing the `clarity` plugin, you can run:

```bash
pytest -x -vv
```

## Security

### Bandit (Security Analysis)

To check a Python file for security issues using `Bandit`:

```bash
bandit file.py
```

### Checking All Files in a Folder

To check all files within a folder:

```bash
bandit -r folder/
```

### Skipping Lines from Security Checks

To skip checking a specific line, add `# nosec` to the concerned line.
