# wc.py
import argparse
import sys

def word_count(input_text):
    lines = input_text.split('\n')
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = len(input_text)

    return line_count, word_count, char_count

def main():
    parser = argparse.ArgumentParser(description='Word count utility')
    parser.parse_args()  # Currently, no arguments are needed

    input_text = sys.stdin.read()
    line_count, word_count, char_count = word_count(input_text)

    print(f"{line_count}\t{word_count}\t{char_count}")

if __name__ == "__main__":
    main()
