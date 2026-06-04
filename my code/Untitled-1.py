# Read input and compute maximum number of Katryoshkas
import sys

def can_make(t, n, m, k):
    if k < t:
        return False
    mouths_used = min(m, t)
    eyes_needed = 2*t - mouths_used
    return n >= eyes_needed

def max_katryoshkas(n, m, k):
    lo, hi = 0, k
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_make(mid, n, m, k):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    n, m, k = map(int, data[:3])
    print(max_katryoshkas(n, m, k))
