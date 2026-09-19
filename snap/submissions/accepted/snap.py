def solve(M: int, N: int, F: int, S: list[str]) -> None:
	min_x = N
	min_y = M
	max_x = 0
	max_y = 0
	for i in range(M):
		for j in range(N):
			if S[i][j] != '.':
				min_x = min(min_x, j)
				min_y = min(min_y, i)

				max_x = max(max_x, j)
				max_y = max(max_y, i)

	if (max_x - min_x > F) or (max_y - min_y > F):
		print('IMPOSSIBLE')
	else:
		for i in range(min_y, min_y + F):
			if (i >= M): continue
			curr_s = ''
			for j in range(min_x, min_x + F):
				if (j >= N): continue
				curr_s += S[i][j]
			print(curr_s)

def main():
	T = int(input())
	for _ in range(T):
		temp = input().split()
		M = int(temp[0])
		S = []
		for _ in range(M):
			S.append(input())
		solve(M, int(temp[1]), int(temp[2]), S)

if __name__ == '__main__':
	main()