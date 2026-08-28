def fibonacci(n):
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
n = int(input("Enter the number of terms: "))

print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i), end=" ")