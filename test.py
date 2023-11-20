# test.py
import os
import subprocess
import sys

def run_test(program, name):
    input_path = f"test/{program}.{name}.in"
    output_path = f"test/{program}.{name}.out"
    arg_output_path = f"test/{program}.{name}.arg.out"
    status_path = f"test/{program}.{name}.status"
    err_output_path = f"test/{program}.{name}.err"
    arg_err_output_path = f"test/{program}.{name}.arg.err"
    timeout_path = f"test/{program}.{name}.timeout"

    # Set up the command to run
    command = ["python", f"prog/{program}.py", input_path]
    
    # Check if argument mode is specified
    if os.path.exists(arg_output_path):
        command = ["python", f"prog/{program}.py", input_path]

    # Check if timeout is specified
    timeout = None
    if os.path.exists(timeout_path):
        timeout = int(open(timeout_path).read().strip())

    try:
        # Run the command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout)
        
        # Check exit status
        expected_status = int(open(status_path).read().strip()) if os.path.exists(status_path) else 0
        assert result.returncode == expected_status, f"Exit status mismatch for {program}.{name}"

        # Check STDOUT
        expected_output = open(output_path).read().strip() if os.path.exists(output_path) else ""
        assert result.stdout.strip() == expected_output, f"Output mismatch for {program}.{name}"

        # Check STDERR
        expected_err_output = open(err_output_path).read().strip() if os.path.exists(err_output_path) else ""
        assert result.stderr.strip() == expected_err_output, f"Error output mismatch for {program}.{name}"

        # Check argument mode STDERR
        if os.path.exists(arg_err_output_path):
            result_arg = subprocess.run(command + [input_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout)
            expected_err_output_arg = open(arg_err_output_path).read().strip()
            assert result_arg.stderr.strip() == expected_err_output_arg, f"Error output mismatch for {program}.{name} in argument mode"
    
    except subprocess.TimeoutExpired:
        raise TimeoutError(f"Test {program}.{name} timed out after {timeout} seconds")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Run tests for wc
    run_test("wc", "simple")

    # Run tests for gron
    run_test("gron", "basic")

    # Run tests for csv_sum
    run_test("csv_sum", "simple")
