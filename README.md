# Build Number Incrementer

This project provides a Python script to automate the process of incrementing the build number in both `Info.plist` and `build.gradle` files. This is particularly useful for developers who need to manage versioning in their applications efficiently.

## Project Structure

```
build-number-incrementer
├── src
│   ├── increment_build_number.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   cd build-number-incrementer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To increment the build number, run the following command in your terminal:

```
python src/increment_build_number.py
```

This script will:
- Read the current build number from `Info.plist` and `build.gradle`.
- Increment the build number by 1.
- Write the updated build number back to both files.

## Requirements

Make sure you have Python installed on your machine. The script may require additional libraries for XML and Gradle file manipulation, which are listed in `requirements.txt`.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.
