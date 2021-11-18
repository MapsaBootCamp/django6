from pathlib import Path



print(Path(__file__).resolve().parent.parent)

BASE_DIR = Path(__file__).resolve().parent

USER_DATA_PATH = BASE_DIR / "users_data"
BOOKS_DATA_PATH = BASE_DIR / "books_data"



