def solve(N, R, A):
	assert N == len(A), f'N={N}, len(A)={len(A)}'
	assert N <= 1000
	assert R <= 1000
	for a in A:
		assert a <= 10000, f'a={a}'
	
def main():
	T = int(input())
	assert T <= 100
	for _ in range(T):
		temp = input().split()
		N = int(temp[0])
		R = int(temp[1])
		A = list(map(int, input().split()))
		print(solve(N, R, A))

if __name__ == '__main__':
	main()