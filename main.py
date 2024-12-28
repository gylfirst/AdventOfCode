from pathlib import Path
from dotenv import load_dotenv
from utils.inputs import store_input
import os
import importlib.util

if __name__ == "__main__":
    load_dotenv()
    year = input("Enter the year: ")
    day = input("Enter the day: ")

    folder_path = Path(f"{year}/{day}")

    solution_path = folder_path.joinpath("solution.py")
    input_path = folder_path.joinpath("input.txt")

    if not folder_path.exists():
        print(f"Folder '{folder_path}' does not exist.")
        exit(1)

    if not solution_path.exists():
        print(f"File '{solution_path}' does not exist.")
        exit(1)

    session_cookie = os.getenv("SESSION_COOKIE")
    if not session_cookie:
        print("SESSION_COOKIE not found in .env file.")
        exit(1)
    store_input(year, day, session_cookie)

    print(f"Reading input from '{input_path}'...")
    input_value = input_path.read_text()

    print(f"Executing '{solution_path}'...")
    spec = importlib.util.spec_from_file_location("solution", solution_path)
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)

    answer_part1 = solution_module.solution_1(input_value)
    print(f"Answer for part 1: {answer_part1}")

    answer_part2 = solution_module.solution_2(input_value)
    print(f"Answer for part 2: {answer_part2}")
