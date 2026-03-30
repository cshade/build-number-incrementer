#!/usr/bin/env python3


def increment_build_number(plist_path, gradle_path):
    import plistlib
    import re

    # Increment build number in Info.plist
    with open(plist_path, "rb") as plist_file:
        plist_data = plistlib.load(plist_file)
        current_build_number = int(plist_data["CFBundleVersion"])
        new_build_number = current_build_number + 1
        plist_data["CFBundleVersion"] = str(new_build_number)

    with open(plist_path, "wb") as plist_file:
        plistlib.dump(plist_data, plist_file)

    print(
        "Updated iOS build number "
        f"from {current_build_number} to {new_build_number} in {plist_path}"
    )

    # Increment build number in build.gradle
    with open(gradle_path, "r") as gradle_file:
        gradle_content = gradle_file.read()

    new_gradle_content = re.sub(
        r'versionName\s+"(\d+\.\d+\.\d+)"',
        lambda match: f'versionName "{match.group(1)}"',
        gradle_content,
    )
    new_gradle_content = re.sub(
        r"versionCode\s+(\d+)",
        f"versionCode {new_build_number}",
        new_gradle_content,
    )

    with open(gradle_path, "w") as gradle_file:
        gradle_file.write(new_gradle_content)

    print(f"Updated Android build number to {new_build_number} in {gradle_path}")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Increment iOS and Android build numbers"
    )
    parser.add_argument(
        "--plist", default="./ios/App/App/Info.plist", help="Path to Info.plist"
    )
    parser.add_argument(
        "--gradle", default="./android/app/build.gradle", help="Path to build.gradle"
    )
    args = parser.parse_args()

    increment_build_number(args.plist, args.gradle)


if __name__ == "__main__":
    main()
