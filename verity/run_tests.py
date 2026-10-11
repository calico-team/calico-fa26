
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

    # Start the interactor.
    with open(log_file, "w") as log:
        interactor = subprocess.Popen(
            [
                sys.executable,
                "-u",
                str(INTERACTOR),
                str(test_file),
                str(log_file),
            ],
            cwd=ROOT,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=None,
            text=True,
            bufsize=1,
        )

        sol = None

        try:
            # Connect interactor -> solution and solution -> interactor.
            sol = subprocess.Popen(
                [str(BINARY)],
                cwd=ROOT,
                stdin=interactor.stdout,
                stdout=interactor.stdin,
                stderr=None,
                text=True,
                bufsize=1,
            )

            # The parent must not keep extra copies of the pipe ends.
            interactor.stdout.close()
            interactor.stdin.close()

            # Both processes must finish.
            sol.wait(timeout=TIMEOUT)
            interactor.wait(timeout=TIMEOUT)

        except subprocess.TimeoutExpired:
            print("TIMEOUT")
            for proc in (sol, interactor):
                if proc is not None and proc.poll() is None:
                    proc.kill()

            for proc in (sol, interactor):
                if proc is not None:
                    try:
                        proc.wait(timeout=1)
                    except subprocess.TimeoutExpired:
                        pass

            print(f"  See {log_file.name} for the interaction log.")
            return False

        except Exception as exc:
            print(f"RUNNER ERROR: {exc}")
            for proc in (sol, interactor):
                if proc is not None and proc.poll() is None:
                    proc.kill()
            for proc in (sol, interactor):
                if proc is not None:
                    proc.wait()
            return False

    # Check the judge's actual verdict, not just its exit code.
    try:
        verdict = log_file.read_text().splitlines()
    except OSError:
        print("FAILED: Could not read verdict log.")
        return False

    if verdict and verdict[0].strip() == "AC":
        print("ACCEPTED")
        return True

    print("WRONG ANSWER" if verdict and verdict[0].strip() == "WA"
          else "FAILED")
    print(f"  See {log_file.name} for details.")
    return False


def main():
    os.chdir(ROOT)

    test_files = sorted(ROOT.glob("data/*/*.in"))

    if not test_files:
        print("ERROR: No tests found under data/*/*.in")
        sys.exit(1)

    compile_solution()

    for test_file in test_files:
        if not run_test(test_file):
            sys.exit(1)

    print("\nAll test cases passed successfully!")


if __name__ == "__main__":
    main()
