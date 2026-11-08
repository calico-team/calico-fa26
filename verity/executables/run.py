#!/usr/bin/env python3
import io
import random
import sys

_log = []


def run():
    log("Interaction problem is active")

    T = int(input_test_in())
    print_prog(T)

    for case in range(1, T + 1):
        log(f"Begin test case #{case} of {T}")

        N, K = map(int, input_test_in().split())
        alphabet = input_test_in().split()

        solution = "".join(random.choice(alphabet) for _ in range(N))

        print_prog(f"{N} {K}")
        print_prog(" ".join(alphabet))

        num_guesses = 0

        while True:
            if num_guesses > 100:
                give_WA("Exceeded maximum number of allowed guesses.")

            guess = str(input_prog())
            num_guesses += 1

            if len(guess) != N:
                give_WA(f"Invalid guess length: expected {N}, got {len(guess)}")

            if guess == solution:
                print_prog("CORRECT")
                break

            feedback = []
            for i in range(N):
                if guess[i] not in alphabet:
                    give_WA(f'Invalid character: "{guess[i]}"')
                if guess[i] == solution[i]:
                    feedback.append(solution[i])
                else:
                    feedback.append("_")

            print_prog("".join(feedback))

    give_AC()


def main():
    if len(sys.argv) < 2:
        print("Usage: run.py input_file", file=sys.stderr)
        sys.exit(2)

    with open(sys.argv[1], "r") as test_in:
        global _test_in
        _test_in = test_in
        run()


def give_AC():
    try:
        while True:
            extra = input().strip()
            if extra:
                give_WA(f"Unexpected trailing output: {extra}")
    except EOFError:
        pass

    sys.exit(42)


def give_WA(reason):
    log("End of log")
    print(f"WA: {reason}", file=sys.stderr)
    for line in _log:
        print(line, file=sys.stderr)
    sys.exit(43)


def give_IE(reason):
    print(f"Interactor error: {reason}", file=sys.stderr)
    sys.exit(2)


def input_test_in():
    line = _test_in.readline()
    if line == "":
        give_IE("Unexpected end of test input")
    return line.strip()


def input_prog():
    try:
        line = input()
        _log_without_tabs(f"\t{line}")
        return line
    except EOFError:
        give_WA("Solution exited before completing the interaction")


def print_prog(*args, **kwargs):
    output = io.StringIO()
    print(*args, **kwargs, file=output, end="")

    try:
        print(*args, **kwargs, flush=True)
        _log_without_tabs(output.getvalue())
    except BrokenPipeError:
        give_WA("Solution terminated before receiving judge input")


def log(message):
    _log_without_tabs(f"\t\t{message}")


def _log_without_tabs(message):
    if len(message) > 200:
        message = message[:200] + " (truncated)"
    _log.append(message)


if __name__ == "__main__":
    main()
