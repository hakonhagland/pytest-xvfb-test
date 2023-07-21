import myproject.main

from myproject.main import MainWindow
from typing import Any

QtBot = Any  # Missing type hints here

def test_app(qtbot: QtBot) -> None:
    window = myproject.main.create_window()
    assert isinstance(window, MainWindow)
