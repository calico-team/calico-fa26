from collections import deque

def solve(N, R, A):
	dq = deque([0, 0])

	for a in A:
		r = dq.popleft()
		if r <= a:
			dq.append(r + R)
		else:
			return "NO"
	return "YES"

def main():
	T = int(input())
	for _ in range(T):
		temp = input().split()
		N = int(temp[0])
		R = int(temp[1])
		A = list(map(int, input().split()))
		print(solve(N, R, A))

if __name__ == '__main__':
	main()