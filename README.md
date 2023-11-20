# python-test-harness

## NAME: ARCHA PATEL
## Login Id: apatel20@stevens.edu

## Project Description

This project involves the implementation of three command-line utilities in Python: `wc` (word count), `gron` (JSON flattening), and a custom utility `csv_sum` (CSV column sum). Additionally, a test harness is created using Python to test these utilities, and continuous integration is set up using GitHub Actions.

## Directory Structure

/
README.md # Project description
test.py # Test harness
prog/
wc.py # Word count utility
gron.py # JSON flattening utility
csv_sum.py # CSV column sum utility
... # Other program files
test/
wc.simple.in # Input for test case 'simple' on program wc
wc.simple.out # Expected output for test case 'simple' on program wc
wc.simple.arg.out # Expected output with argument input for program wc
gron.basic.in
gron.basic.out
gron.basic.arg.out
csv_sum.simple.in
csv_sum.simple.out
csv_sum.simple.arg.out
.github/
workflows/
test.yaml 

## Extensions Implemented
Extension 1 : More advanced wc: multiple files

# prog/wc.py
import argparse
import sys

def wc(file_paths):
    total_lines = total_words = total_characters = 0

    for file_path in file_paths:
        lines = words = characters = 0

        with open(file_path, 'r') as file:
            for line in file:
                lines += 1
                words += len(line.split())
                characters += len(line)

        print(f"{lines}\t{words}\t{characters} {file_path}")

        total_lines += lines
        total_words += words
        total_characters += characters

    print(f"{total_lines}\t{total_words}\t{total_characters} total")

def main():
    parser = argparse.ArgumentParser(description="Word count utility")
    parser.add_argument("files", nargs="+", help="Input files")
    args = parser.parse_args()

    try:
        wc(args.files)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

## Extension 2 : More advanced wc: flags to control output

# prog/wc.py
import argparse
import sys

def wc(file_paths, lines_flag=False, words_flag=False, characters_flag=False):
    total_lines = total_words = total_characters = 0

    for file_path in file_paths:
        lines = words = characters = 0

        with open(file_path, 'r') as file:
            for line in file:
                lines += 1
                words += len(line.split())
                characters += len(line)

        output = f"{file_path}"
        if lines_flag:
            output += f"\t{lines}"
        if words_flag:
            output += f"\t{words}"
        if characters_flag:
            output += f"\t{characters}"

        print(output)

        total_lines += lines
        total_words += words
        total_characters += characters

    if len(file_paths) > 1:
        total_output = "total"
        if lines_flag:
            total_output += f"\t{total_lines}"
        if words_flag:
            total_output += f"\t{total_words}"
        if characters_flag:
            total_output += f"\t{total_characters}"
        print(total_output)

def main():
    parser = argparse.ArgumentParser(description="Word count utility")
    parser.add_argument("files", nargs="+", help="Input files")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines only")
    parser.add_argument("-w", "--words", action="store_true", help="Count words only")
    parser.add_argument("-c", "--characters", action="store_true", help="Count characters only")
    args = parser.parse_args()

    try:
        wc(args.files, args.lines, args.words, args.characters)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
    
## Extension 3 : More advanced gron: control the base-object name

# prog/gron.py
import argparse
import json
import sys

def flatten_json(obj, base_obj_name='json', sep='_'):
    items = []
    for k, v in obj.items():
        new_key = f"{base_obj_name}{sep}{k}" if base_obj_name else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, base_obj_name=new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def gron(file_path, base_obj_name='json'):
    with open(file_path, 'r') as file:
        data = json.load(file)

    flat_data = flatten_json(data, base_obj_name)

    for key, value in flat_data.items():
        print(f"{key} = {value};")

def main():
    parser = argparse.ArgumentParser(description="JSON flattening utility")
    parser.add_argument("file", help="Input file")
    parser.add_argument("--obj", help="Specify a different base object name")
    args = parser.parse_args()

    try:
        gron(args.file, args.obj)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()


## Testing Approach

Our testing approach focuses on ensuring the correctness and reliability of each command-line utility. Key aspects of our testing strategy include:

Input Variation: We designed tests to cover a range of input scenarios, including edge cases, normal cases, and potential error cases.
Command-Line and STDIN Testing: We tested both command-line input and STDIN input to ensure the utilities work seamlessly in different usage scenarios.
Extension Testing: For the implemented extensions, we crafted specific tests to verify their correct functionality.

## Known Issues
No known issues at the time of submission.

## Resolved Bugs
Bug: Incorrect CSV Sum for Non-Numeric Values
Description: The csv_sum utility was summing columns even if some values were non-numeric, leading to unexpected results.

Resolution: Modified the csv_sum implementation to skip non-numeric values in the specified columns, ensuring accurate summation.

## Estimated Hours Spent
Approximately 27 hours spent on the project.
