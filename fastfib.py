def fastfib(num, memo):
	if num not in memo:
		memo[num] = fastfib(num-1, memo) + fastfib(num-2, memo)
	return memo[num]

def fib(num):
	memo = {0:1, 1:1}
	return fastfib(num, memo)


print(fib(9))