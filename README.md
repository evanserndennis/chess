# chess

A chess project in Python.

## Setup

Requires Python 3.12+.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## Development

```powershell
pytest            # run tests
ruff check .      # lint
ruff format .     # format
```
