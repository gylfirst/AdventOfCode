from requests import get
from pathlib import Path


def get_input(year: int, day: int, session_cookie) -> str:
    return get(
        url=f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": session_cookie},
    ).text


def store_input(year: int, day: int, session_cookie) -> None:
    input_path = Path(f"{year}/{day}/input.txt")
    if not input_path.exists():
        print(f"File '{input_path}' does not exist.\nStoring input...")
        input_value = get_input(year, day, session_cookie)
        with open(f"{year}/{day}/input.txt", "w") as f:
            f.write(input_value.rstrip("\n"))
            print(f"Input for year {year}, day {day} stored in '{input_path}'")


def store_answer(year: int, day: int, answer: str) -> None:
    answer_path = Path(f"{year}/{day}/answers.txt")
    if not answer_path.exists():
        print(f"File '{answer_path}' does not exist.\nStoring answer...")
        with open(f"{year}/{day}/answers.txt", "w") as f:
            f.write(answer)
            print(f"Answers for year {year}, day {day} stored in '{answer_path}'")
