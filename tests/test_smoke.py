import inspect

import starlette_testclient


def test_smoke() -> None:
    assert inspect.ismodule(starlette_testclient)
