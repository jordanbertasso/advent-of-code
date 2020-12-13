adaps = []
with open('input.txt', 'r') as f:
    adaps = f.readlines()
    adaps = list(map(int, adaps))

adaps.append(0)
adaps.sort()
n = len(adaps)
dp = [0] * n
dp[0] = 1

for i in range(1, n):
    for j in range(i):
        if (adaps[i] - adaps[j] <= 3):
            dp[i] += dp[j]

print(dp[n - 1])
