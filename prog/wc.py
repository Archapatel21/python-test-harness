# wc.py
import argparse
import sys

def wc(file_path):
    # Implement wc functionality
    pass

def main():
    parser = argparse.ArgumentParser(description="Word count utility")
    parser.add_argument("file", nargs="?", default="-", help="Input file")
    args = parser.parse_args()

    try:
        result = wc(args.file)
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
