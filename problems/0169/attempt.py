from functools import lru_cache


@lru_cache(None)
def F(n, k, c):
    if n <= 0 or k <= 0:
        return 0
    else:
        if k < n:
            return c + 0
        else:
            if k == n:
                return c + 1
            else:
                return c + F(n - 1, k - 1, c) + F(n + 1, k - 1, c)


N, K = map(int, input().split())
print(F(N, K, 0))