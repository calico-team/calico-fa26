def solve(S: str) -> str:
	if "write_me" in S:
		return S + "make_it_sound_human"
	if "what_is" in S:
		return S + "do_not_hallucinate"
	if "solve" in S:
		return S + "make_no_mistakes"
	return S + "thank_you"

def main():
	T = int(input())
	for _ in range(T):
		S = input()
		print(solve(S))

if __name__ == "__main__":
	main()