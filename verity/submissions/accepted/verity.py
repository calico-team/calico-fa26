def solve(N: int, K: int, A: list[str]):
	guess = '_' * N
	for _ in range(K):
		for i in range(N):
			new_guess = ''
			if guess[i] == '_':
				new_guess += A[i]
			else:
				new_guess += guess[i]

		print(new_guess)
		guess = input()
		if guess == 'CORRECT':
			return


def main():
	T = int(input())
	assert T <= 100
	for _ in range(T):
		temp = input().split()
		N, K = int(temp[0]), int(temp[1])
		A = input().split()

		solve(N, K, A)


if __name__ == '__main__':
	main()