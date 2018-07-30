# Complete the maxDifference function below.
def maxDifference(a):
    max_diff = -1
    min_before = a[0]
    for i in a[1:]:
        if i-min_before > 0:
            max_diff = max(max_diff, i-min_before)
        min_before = min(min_before, i)
    return max_diff