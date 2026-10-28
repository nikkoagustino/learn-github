# Learn GitHub

A beginner repository for practicing GitHub pull requests, code review, and GitHub Actions automation with a small Python math project.

## Project structure

```text
learn-github/
├── .github/
│   └── workflows/          # Your GitHub Actions workflows go here
├── math_utils/
│   ├── __init__.py         # Package exports
│   └── calculator.py       # Math functions, including known defects
├── tests/                  # Create pytest files here
├── pyproject.toml          # pytest configuration
└── requirements.txt        # Python test dependency
```

## Set up locally

```bash
python -m pip install -r requirements.txt
```

## Starter functions

- `add`: intended to return the sum and should be passing.
- `multiply`: intended to return the product and should be passing.
- `subtract`: intentionally returns incorrect results for some inputs.
- `divide`: intentionally returns incorrect results for some inputs.

Do not copy a test from a solution or remove failing cases only to make the suite pass. Use normal test values, edge cases, and an appropriate expected result for each function.

## Test suite exercise

1. Create a test file under the `tests/` folder, for example `tests/test_calculator.py`.
2. Write tests for `add`, `subtract`, `multiply`, and `divide`.
3. Include a divide-by-zero test using `pytest.raises`.
4. Run the suite locally with `python -m pytest`.
5. Expect the suite to report failures for the functions with defects.

## Pull request exercise

1. Create a new branch, such as `test/add-calculator-tests`.
2. Add your own test suite.
3. Run `python -m pytest` locally.
4. Commit the tests and open a pull request into the main branch.
5. Ask another person to review the tests, cases covered, and failure output.

## GitHub Actions exercise

Create `.github/workflows/tests.yml` yourself.

The workflow should:

1. Run when a pull request targets the main branch.
2. Run on an Ubuntu runner.
3. Check out the repository.
4. Set up Python.
5. Install `requirements.txt`.
6. Run `python -m pytest`.

This workflow should run the coworker's test suite automatically. A failing test is useful here because it demonstrates that automation detected a defect in the pull request code.
