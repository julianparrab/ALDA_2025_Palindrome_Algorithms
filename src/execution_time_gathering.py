import time
import random
from src import algorithms
from src import constants
from src import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size, ensure_palindrome, recursive):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size, ensure_palindrome, recursive)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size, ensure_palindrome, recursive):
    samples = [data_generator.get_random_strings(size, samples_by_size, ensure_palindrome)]
    if recursive == False :
        return  [
            take_time_for_algorithm(samples, algorithms.is_palindrome_iterative),
            take_time_for_algorithm(samples, algorithms.is_palindrome_reverse),
            take_time_for_algorithm(samples, algorithms.is_palindrome_join_reverse),
            take_time_for_algorithm(samples, algorithms.is_palindrome_stack_queue),
        ]
    else:
        return [
            take_time_for_algorithm(samples, algorithms.is_palindrome_recursive),
        ]



"""
    Returns the median of the execution time measures for a sorting approach given in 
"""


def take_time_for_algorithm(samples_array, algorithm):
    times = []
    # print("samples_array: " + str(samples_array))
    for sample in samples_array:
        # print("sample: " + str(sample))
        for s in sample:
            # print("s: " + str(s))
            start_time = time.time()
            res = algorithm(s)
            #print("res: " + str(res))
            times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]
