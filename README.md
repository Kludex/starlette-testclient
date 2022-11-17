<h1 align="center">
    <strong>starlette-testclient</strong>
</h1>
<p align="center">
    <a href="https://github.com/Kludex/starlette-testclient" target="_blank">
        <img src="https://img.shields.io/github/last-commit/Kludex/starlette-testclient" alt="Latest Commit">
    </a>
        <img src="https://img.shields.io/github/workflow/status/Kludex/starlette-testclient/CI">
        <a href="https://github.com/Kludex/starlette-testclient/actions?workflow=CI" target="_blank">
            <img src="https://img.shields.io/badge/Coverage-100%25-success">
        </a>
    <br />
    <a href="https://pypi.org/project/starlette-testclient" target="_blank">
        <img src="https://img.shields.io/pypi/v/starlette-testclient" alt="Package version">
    </a>
    <img src="https://img.shields.io/pypi/pyversions/starlette-testclient">
    <img src="https://img.shields.io/github/license/Kludex/starlette-testclient">
</p>

This is a backport of Starlette's `TestClient` using `requests` instead of `httpx`.

The reason behind here is to give more time for people to migrate.

## Installation

```bash
pip install starlette-testclient
```

## Usage

You just need to replace the import statement from:

```python
from starlette.testclient import TestClient
```

to:

```python
from starlette_testclient import TestClient
```

Easy, right? :sweat_smile:

## License

This project is licensed under the terms of the BSD 3-Clause license.
