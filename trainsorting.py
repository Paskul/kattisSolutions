n = int(input())
v = []
for i in range(n):
    v.append(int(input()))

ans = 0

# Longest Increasing Subsequence starting at each index
longestIncreasingSubsequence = [1] * n 
# Longest Decreasing Subsequence starting at each index
longestDecreasingSubsequence = [1] * n 

# Compute LIS and LDS starting from each index

# from last car, to starting car
for i in range(n - 1, -1, -1):

    # from last car, to car that was chosen above
    for j in range(n - 1, i, -1):

        # if j-car can be added after i-car to extend increasing subsequence
        # then increasing suebseqnce is updated as a increasingSubsequence+1 (at it's index)
        if v[j] > v[i]:
            longestIncreasingSubsequence[i] = max(longestIncreasingSubsequence[i], longestIncreasingSubsequence[j] + 1)

        # same but in reverse
        # if j-car can be added before i-car to extend decreasing subsequence
        # then decreasing suebseqnce is updated as a decreasingSubsequence+1 (at it's index)
        if v[j] < v[i]:
            longestDecreasingSubsequence[i] = max(longestDecreasingSubsequence[i], longestDecreasingSubsequence[j] + 1)

    # minus one, because car at i is counted twice
    ans = max(ans, longestIncreasingSubsequence[i] + longestDecreasingSubsequence[i] - 1)

print(ans)
