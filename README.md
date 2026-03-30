# Build Number Incrementer

This project provides a Python script to automate the process of incrementing the build number in both `Info.plist` and `build.gradle` files. This is useful for developers who do not have an automated pipeline utility that manages their versioning and so they manually bump the build number for incremental deployments to Apple and Google.

## Project Structure

```text
build-number-incrementer
├── src
│   ├── increment_build_number.py
├── tests
│   ├── test_increment_build_number.py
├── package.json
├── pyproject.toml
└── README.md
```

## Requirements

- **Python**: Make sure Python 3.8+ is installed on your machine.
- **Node.js**: Required for the `npm link` setup (for the JS wrapper/CLI in this repo).

## Installation

1. Clone the repository to your local machine:

```bash
git clone <repository-url>
cd build-number-incrementer
```

2. Install the Python package and dev dependencies:

```bash
pip install -e .
pip install -e .[dev]
```

3. Install the Git hooks:

```bash
pre-commit install
```

4. (Optional) Set up the project as a global npm package using `npm link`:

```bash
npm link
```

This will make the `increment-build-number` command globally available on your system.

## Usage

To increment the build number, given that the script assumes the relative paths, navigate to the root of your project (the one containing `Info.plist` and `build.gradle`) and run:

```bash
increment-build-number
```

Or add an npm script to your `package.json`:

```json
{
  "scripts": {
    "increment-build": "increment-build-number"
  }
}
```

And then run the script:

```bash
npm run increment-build
```

This script will:

- Read the current build number from `Info.plist` and `build.gradle`.
- Increment the build number by 1.
- Write the updated build number back to both files.

## Running Tests

This project uses [pytest](https://pytest.org/) for unit testing. All tests are located in the `tests/` folder.

To run all tests, use:

```bash
pytest
```

If needed, install pytest from pyproject dev deps:

```bash
pip install -e .[dev]
```

Test files are named with the pattern `test_*.py` and cover the main functionality of the scripts in `src/`.

## Code Quality

This project uses [pre-commit](https://pre-commit.com/) with a minimal Python hook set:

- `ruff check --fix` for linting and import cleanup
- `ruff format` for formatting

Run the full hook suite locally with:

```bash
pre-commit run --all-files
```

If you only want to run the Python test suite:

```bash
pytest
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

MIT
