# tests/test_main.py
from templates.python.standard.src.app.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out