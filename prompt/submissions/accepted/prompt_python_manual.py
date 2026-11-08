def solve(S: str) -> str:
    """
    Output the result of adding a certain string to the end of a prompt.

    S: Original prompt
    """

    p1 = "write_me"
    p2 = "what_is"
    p3 = "solve"

    "This is a solution where we manually iterate through the string"
    i = 0
    while (i < len(S) - len(p1)):
        if (S[i: i + len(p1)] == p1):
              return S + "make_it_sound_human"
        i += 1

    i = 0
    while (i < len(S) - len(p2)):
        if (S[i: i + len(p2)] == p2):
                return S + "do_not_hallucinate"
        i += 1

    i = 0
    while (i < len(S) - len(p3)):
        if (S[i: i + len(p3)] == p3):
                return S + "make_no_mistakes"
        i += 1

    return S + "thank_you"

def main():
	T = int(input())
	for _ in range(T):
		S = input()
		print(solve(S))

if __name__ == "__main__":
	main()