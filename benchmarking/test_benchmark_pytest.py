# Benchmarking with pytest-benchmark
# installation : pip install pytest pytest-benchmark

def test_builtin_sum(benchmark):
    benchmark(sum, range(1_000_000))

def test_manual_loop(benchmark):
    def manual():
        x = 0
        for i in range(1_000_000):
            x += i
        return x
    
    benchmark(manual)