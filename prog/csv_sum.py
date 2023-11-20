# csv_sum.py
import argparse
import csv
import sys

def csv_sum(file_path, columns):
    total = 0

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)

        if header is None:
            raise ValueError("CSV file is empty")

        for row in reader:
            for col in columns:
                try:
                    total += float(row[col])
                except (ValueError, IndexError):
                    print(f"Error: Invalid value in column {col}, skipping row.")
    
    return total

def main():
    parser = argparse.ArgumentParser(description="CSV column sum utility")
    parser.add_argument("file", help="CSV file")
    parser.add_argument("columns", nargs="+", type=int, help="Columns to sum")
    args = parser.parse_args()

    try:
        result = csv_sum(args.file, args.columns)
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
