import time
import functools
def cache(func):
    cache_data = {}
    print(cache_data)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args + tuple(sorted(kwargs))
        if key not in cache_data:
            print('not kashed')
            cache_data[key] = func(*args, **kwargs)

        return cache_data[key]
    return inner



@cache
def initialize_settings(file_name):
    with open(file_name) as file:
        print(file.read())
    print('this function load file "{}" only one time'.format(file_name))

initialize_settings('benchmark_results.txt')