# Advent of Code Solutions

Welcome to my GitHub repository for Advent of Code solutions! This repository contains my solutions for the Advent of Code challenges, implemented in Python.

## About Advent of Code

[Advent of Code](https://adventofcode.com/) is an annual event in December, where each day a new programming challenge is released. It's a great way to improve your coding skills and have fun solving problems.

## Repository Structure

Each year's solutions are organized into separate directories. Within each directory, you'll find the solutions for each day's challenge.

```
.
├── year (2024)
│   ├── day (1)
│   │   ├── text.md
│   │   └── solution.py
│   ├── day (2)
│   │   ├── text.md
│   │   └── solution.py
│   └── ...
├── .env
├── init_script.sh
└── README.md
```

## How to Run

### Generate all working files

If you want to work on a new year, you can create all folders and files (`solution.py` and `text.md`) simply using the initialisation script.

For example for 2024:

```sh
chmod +x init_script.sh
./init_script.sh 2024
```

### Get your session cookie

Get your session cookie from your browser, using the inspector in Network tab. Rename the `.env.example` to `.env` and fill it with your cookie.

### Get the solution

To run the solutions, you need to have Python installed. Execute the main program, enter the year and the day, it will execute the right file and give you the solution, after downloading the input values, using your session cookie.

Example for the 1st December 2024:

```sh
python main.py
```

```py
"Enter the year:" 2024
"Enter the day:" 1
"File '2024/1/input.txt' does not exist."
"Storing input..."
"Input for year 2024, day 1 stored in '2024/1/input.txt'"
"Reading input from '2024/1/input.txt'..."
"Executing '2024/1/solution.py'..."
"Answer for part 1:" answer_p1
"Answer for part 2:" answer_p2
```

## Acknowledgments

- [Advent of Code](https://adventofcode.com/) for providing the challenges.
