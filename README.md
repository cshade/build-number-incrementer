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
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository to your local machine:

```bash
git clone <repository-url>
cd build-number-incrementer
```

1. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

1. Set up the project as a global npm package using `npm link`:

```bash
npm link
```

This will make the `increment-build-number` command globally available on your system.

## Usage

To increment the build number, navigate to the root of your project (the one containing `Info.plist` and `build.gradle`) and run:

```bash
increment-build-number ./ios/App/App/Info.plist ./android/app/build.gradle
```

Or add an npm script to your `package.json`:

```json
{
  "scripts": {
    "increment-build": "increment-build-number ../ios/App/App/Info.plist ../android/app/build.gradle"
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

If you need to install pytest, run:

```bash
pip install -r requirements.txt
```

Test files are named with the pattern `test_*.py` and cover the main functionality of the scripts in `src/`.

## Requirements

- **Python**: Make sure Python is installed on your machine.
- **Node.js**: Required for the `npm link` setup.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.