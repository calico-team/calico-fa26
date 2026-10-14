def solve(N, R, A):
	recharging = []
	for a in A:
		while recharging and recharging[0] <= a:
			recharging.pop(0)

		if len(recharging) == 2:
			return 'NO'
		elif len(recharging) == 1:
			recharging.append(recharging[0] + R)
		else:
			recharging.append(a + R)

	return 'YES'

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