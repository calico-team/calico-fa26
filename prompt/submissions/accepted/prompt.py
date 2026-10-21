def solve(S: str) -> str:
	if "write_me" in S:
		return S + "make it sound human"
	if "what_is" in S:
		return S + "do not hallucinate"
	if "solve" in S:
		return S + "make no mistakes"
	return S + "thank you"

def main():
	T = int(input())
	for _ in range(T):
		S = input()
		print(solve(S))

if __name__ == "__main__":
	main()