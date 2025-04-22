import time
def speed_calc_decorator(function):

    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        run_time = end_time -  start_time
        print(f"{function.__name__} ran in {run_time:.4f} seconds")
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

# Run both functions
fast_function()
slow_function()
