# src/utils/env_utils.py
from pathlib import Path
from dotenv import load_dotenv

def load_env(dotenv_path: str | None = None) -> None:
    """
    Load environment variables from .env -> os.environ.
    """
    dotenv_path = dotenv_path or ".env"
    env_file = Path(dotenv_path)
    if env_file.exists():
        load_dotenv(dotenv_path)