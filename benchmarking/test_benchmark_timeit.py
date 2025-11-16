# Benchmark sum function 

import timeit

# number is how many times to run the code snippet; code snippet is in strings
# sum of all ints from 0 to 1M(exluded)
time_10iter = timeit.timeit("sum(range(1_000_000))", number=10)
print("time_10iter --> ", time_10iter) # 0.156 secs
# Interpretation --> 0.156 for 10 iterations so baseline = 15.6 ms / iteration on this machine

# Benchmark 2 implementations
builtin = timeit.timeit("sum(range(1_000_000))", number=10)
loop = timeit.timeit("""
x = 0
for i in range(1_000_000):
    x += i
""", number=10)

print("Builtin sum:", builtin)
print("Manual loop:", loop)
