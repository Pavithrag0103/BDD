import os

file_path = "pytest.ini"

if os.path.exists(file_path):
    os.remove(file_path)
    print("pytest.ini deleted successfully.")
else:
    print("pytest.ini not found.")
