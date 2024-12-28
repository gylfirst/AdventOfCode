# Preparation of the input value for the solution functions
def prepare_list(input_value: str) -> list:
    left, right = [], []
    sol = input_value.split("\n")
    for i in range(len(sol)):
        sol[i] = sol[i].split()
        sol[i] = [int(x) for x in sol[i]]
    for item in sol:
        left.append(item[0])
        right.append(item[1])
    return left, right


# Solution for part 1
def solution_1(input_value: str) -> int:
    distance: int = 0
    left, right = prepare_list(input_value)
    left, right = sorted(left), sorted(right)
    for i in range(len(left)):
        distance += abs(left[i] - right[i])
    return distance


# Solution for part 2
def solution_2(input_value: str) -> int:
    score: int = 0
    left, right = prepare_list(input_value)
    for item in left:
        count = right.count(item)
        score += item * count
    return score
