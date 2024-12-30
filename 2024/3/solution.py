import re


# Sub-Functions for the solution
def get_multiplication(line: str) -> list[str]:
    """
    This function returns the multiplication parts in the given line.

    Args:
        line (str): The line to be parsed.

    Returns:
        list[str]: The list of multiplication parts.
    """
    template = re.compile(r"mul\([0-9]+,[0-9]+\)")
    return template.findall(line)


def multiply(mult_string: str) -> int:
    """
    This function returns the multiplication of the given string.

    Args:
        mult_string (str): The string to be parsed.

    Returns:
        int: The multiplication result.
    """
    template = re.compile(r"[0-9]+")
    a, b = template.findall(mult_string)
    return int(a) * int(b)


def perform_calculation(line: str) -> int:
    """
    This function returns the calculation result of the given line.

    Args:
        line (str): The line to be parsed.

    Returns:
        score (int): The calculation result.
    """
    score: int = 0
    instructions: list[str] = get_multiplication(line)
    for i in range(len(instructions)):
        score += multiply(instructions[i])
    return score


# Solution for part 1
def solution_1(input_value: str) -> int:
    score: int = 0
    for line in input_value.split("\n"):
        score += perform_calculation(line)
    return score


# Solution for part 2
def solution_2(input_value: str) -> int:
    score: int = 0
    total_text = ""
    template_do = re.compile(r"do\(\)")
    template_dont = re.compile(r"don't\(\)")

    # Regroup the text to avoid the split of the do() and don't() functions
    for line in input_value.split("\n"):
        total_text += line

    # Split the text by the do() function
    instructions = re.split(template_do, total_text)

    # Split the remaining text by the don't() function and keep the first part (corresponding to the do)
    for i in range(len(instructions)):
        final_instructions = re.split(template_dont, instructions[i])
        # Perform the multiplication
        score += perform_calculation(final_instructions[0])
    return score
