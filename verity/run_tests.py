
import glob
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = Path(
    sys.argv[1] if len(sys.argv) > 1
    else ROOT / "submissions" / "accepted" / "verity.cpp"
).resolve()
BINARY = ROOT / "verity.bin"
INTERACTOR = ROOT / "executables" / "run.py"
TIMEOUT = 5


def compile_solution():
    if not SOURCE.is_file():
        print(f"ERROR: Solution source not found: {SOURCE}")
        sys.exit(1)

    command = [
        "g++",
        "-std=c++17",
        "-O2",
        "-pipe",
        str(SOURCE),
        "-o",
        str(BINARY),
    ]

    print("Compiling solution...", flush=True)

    try:
        result = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=60,
        )
    except FileNotFoundError:
        print("ERROR: g++ not found. Install a C++ compiler first.")
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("ERROR: Compilation timed out.")
        sys.exit(1)

    if result.returncode != 0:
        print("COMPILATION FAILED")
        print(result.stderr)
        sys.exit(1)

    print("Compilation successful.\n", flush=True)


def run_test(test_file):
    log_file = ROOT / "log.txt"

    print(f"Testing {test_file.relative_to(ROOT)}...", end=" ", flush=True)

    sol = None

    # Redirect interactor's stderr into log_file
    with open(log_file, "w") as log:
        try:
            interactor = subprocess.Popen(
                [
                    sys.executable,
                    "-u",
                    str(INTERACTOR),
                    str(test_file),
                ],
                cwd=ROOT,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=log,
            )

            # Connect solution stdin/stdout directly to interactor pipes
            sol = subprocess.Popen(
                [str(BINARY)],
                cwd=ROOT,
                stdin=interactor.stdout,
                stdout=interactor.stdin,
                stderr=None,
            )

            # Close parent process handle copies so pipes close properly on child exit
            interactor.stdout.close()
            interactor.stdin.close()

            # Wait for completion
            sol.wait(timeout=TIMEOUT)
            interactor.wait(timeout=TIMEOUT)

        except subprocess.TimeoutExpired:
            print("TIMEOUT")
            for proc in (sol, interactor):
                if proc is not None and proc.poll() is None:
                    proc.kill()
                    proc.wait()
            print(f"  See {log_file.name} for the interaction log.")
            return False

        except Exception as exc:
            print(f"RUNNER ERROR: {exc}")
            for proc in (sol, interactor):
                if proc is not None and proc.poll() is None:
                    proc.kill()
                    proc.wait()
            return False

    # Check DOMjudge standard return codes from interactor
    if interactor.returncode == 42:
        print("ACCEPTED")
        return True
    elif interactor.returncode == 43:
        print("WRONG ANSWER")
        print(f"  See {log_file.name} for details.")
        return False
    else:
        print(f"FAILED (Exit Code: {interactor.returncode})")
        print(f"  See {log_file.name} for details.")
        return False
