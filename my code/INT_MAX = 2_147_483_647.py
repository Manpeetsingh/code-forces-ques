INT_MAX = 2_147_483_647
LL_MAX  = 9_223_372_036_854_775_807

n, k, a = map(int, input().split())

# compute k^a safely
p = 1
overflow = False

for _ in range(a):
    if p > LL_MAX // k:
        overflow = True
        break
    p *= k

if overflow:
    print("double")
    exit()

# check result
if n <= INT_MAX // p:
    print("int")
elif n <= LL_MAX // p:
    print("long long")
else:
    print("double")
