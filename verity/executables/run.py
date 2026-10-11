
import sys
import io

_log = []


def parse_query(query_str):
    tokens = query_str.strip().split()
    if not tokens:
        return "", []
    return tokens[0], tokens[1:]


def run():
    log("Interaction problem is active")

    T = int(input_test_in())
    print_prog(T)

    for case in range(1, T + 1):
        log(f"Begin test case #{case} of {T}")

        N, K = map(int, input_test_in().split())
        alphabet = input_test_in().split()
        solution = input_test_in().strip()

        print_prog(f"{N} {K}")
        print_prog(" ".join(alphabet))

        while True:
            cmd, args = parse_query(input_prog())

            if cmd == "?":
                query = args[0]

                feedback = []
                for i in range(N):
                    if query[i] == solution[i]:
                        feedback.append(solution[i])
                    else:
                        feedback.append('.')

                print_prog(''.join(feedback))

            elif cmd == '!':
                if len(args) == 1 and args[0] == solution:
                    break
                else:
                    give_WA('Wrong answer')
            else:
                give_WA("Invalid command")

    give_AC()


def main():
    if len(sys.argv) != 3:
        print("Usage: run.py input_file log_file", file=sys.stderr)
        sys.exit(2)

    _, test_in_path, prog_out_path = sys.argv

    with open(test_in_path, "r") as test_in:
        with open(prog_out_path, "w") as prog_out:
            global _test_in, _prog_out
            _test_in = test_in
            _prog_out = prog_out
            run()


def give_AC():
    try:
        while True:
            extra = input().strip()
            if extra:
                give_WA(f"Unexpected trailing output: {extra}")
    except EOFError:
        pass

    _print_prog_out("AC")
    _prog_out.flush()
    sys.exit(0)


def give_WA(reason):
    log("End of log")
    _print_prog_out("WA")
    _print_prog_out(f"Reason: {reason}")
    _print_prog_out("Interaction Log:")

    for line in _log:
        _print_prog_out(line)

    _prog_out.flush()
    sys.exit(1)


def give_IE(reason):
    print(f"Interactor error: {reason}", file=sys.stderr)
    _print_prog_out("IE")
    _print_prog_out(f"Reason: {reason}")
    _prog_out.flush()
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


def _print_prog_out(*args, **kwargs):
    print(*args, **kwargs, file=_prog_out)


def log(message):
    _log_without_tabs(f"\t\t{message}")


def _log_without_tabs(message):
    if len(message) > 200:
        message = message[:200] + " (truncated)"
    _log.append(message)


if __name__ == "__main__":
    main()
