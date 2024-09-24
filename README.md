# tic-tac-toe

## Introduction 
In this exercise, we'll look at methods and strategies for refactoring legacy code.

We'll start by reading a functional tic-tac-toe to understand the purpose and the missing parts.
To add the missing features, we'll use the test-driven method.
Implement tests that will give us the desired result of the functions, then implement the functions.

We'll then see how to separate the logic in the code so that we're not dependent on a Class. Maybe separate the game part from the user interface part (display, input retrieval, etc.).

## Launch project

```bash
python main.py
```
## Run tests
```bash
python -m unittest test_tic_tac_toe.py
```

## Coverage tests
```bash
coverage run -m unittest test_tic_tac_toe.py
```

or html format

```bash
coverage report
coverage html
```