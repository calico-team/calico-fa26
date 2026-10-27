def solve_phase1(T, N, P):
	return f"---NEW CASE---\n{T} 2\n{N}\n---EXPECTED OUTPUT---\n{' '.join(map(str, P))}"


def main():
	T, phase = map(int, input().split())
	
	assert phase == 1
	for _ in range(T):
		N = int(input())
		P = list(map(int, input().split()))
		A = solve_phase1(T, N, P)

		print(A)


if __name__ == '__main__':
	main()
