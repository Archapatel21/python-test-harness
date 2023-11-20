import argparse
import json
import sys

def flatten_json(json_data, parent_key='', separator='.'):
    flattened = {}
    for k, v in json_data.items():
        new_key = f"{parent_key}{separator}{k}" if parent_key else k
        if isinstance(v, dict):
            flattened.update(flatten_json(v, new_key, separator=separator))
        else:
            flattened[new_key] = v
    return flattened

def main():
    parser = argparse.ArgumentParser(description='JSON flattening utility')
    parser.parse_args()  # Currently, no arguments are needed

    input_json = json.load(sys.stdin)
    flattened_json = flatten_json(input_json)

    for key, value in flattened_json.items():
        print(f"{key} = {json.dumps(value)}")

if __name__ == "__main__":
    main()
