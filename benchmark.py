import time
import benchmark
import duration
import pytest_benchmark
class testing():
    def something(duration=0.000001):
        """
        Function that needs some serious benchmarking.
        """
        time.sleep(12)
        print("done test")
        # You may return anything you want, like the result of a computation
        return 123
    
    def test_my_stuff(benchmark):
        # benchmark something
        result = benchmark(testing.something)
    
        # Extra code, to verify that the run completed correctly.
        # Sometimes you may want to check the result, fast functions
        # are no good if they return incorrect results :-)
        assert result == 123
        benchmark(time.sleep, duration=0.02)
        benchmark(time.sleep, 0.02)
        benchmark(time.sleep, 0.000001)  # way more accurate results!
        print("done test")
    
    def test_with_setup(benchmark):
        benchmark.pedantic(something, setup=my_special_setup, args=(1, 2, 3), kwargs={'foo': 'bar'}, iterations=10, rounds=100)
        print("done test")

    def test_my_stuff(benchmark):
        @benchmark
        def something():  # unnecessary function call
            time.sleep(0.000001)
        return 0
        

def main():
    testing.something(benchmark)
    testing.test_my_stuff(duration)
    testing.test_with_setup(benchmark)
    print("done test")
    
    
main()