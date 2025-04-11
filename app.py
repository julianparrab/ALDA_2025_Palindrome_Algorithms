import sys
from src import algorithms
from src import execution_time_gathering
import matplotlib.pyplot as plt

if __name__ == "__main__":
    minimum_size = 1000
    maximum_size = 20000
    step = minimum_size
    samples_by_size = 10
    ensure_palindrome = False

    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size, ensure_palindrome, False)

    print("Size | Iterative | Reverse | Join_Reverse | Stack_queue")
    for row in table:
        print(row)

    # Get Data for Plot Size vs Execution Time
    sizes = [row[0] for row in table]
    Iterative = [row[1] for row in table]
    Reverse = [row[2] for row in table]
    Join_Reverse = [row[3] for row in table]
    Stack_queue = [row[4] for row in table]

    # Execution for Recursive Algorithm
    minimum_size = 100
    maximum_size = 1500
    step = 50

    table1 = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size, ensure_palindrome, True)

    print("Size | Recursive")
    for row in table1:
        print(row)

    # Get Data for Plot Size vs Execution Time
    sizes1 = [row[0] for row in table1]
    Recursive = [row[1] for row in table1]

    fig, (plt1, plt2) = plt.subplots(2, 1, figsize=(8, 8))

    # Execution Time Plot
    plt1.plot(sizes, Iterative, label="Iterative O(n)", marker="o")
    plt1.plot(sizes, Reverse, label="Reverse O(n)", marker="s")
    plt1.plot(sizes, Join_Reverse, label="Join_Reverse O(n)", marker="d")
    plt1.plot(sizes, Stack_queue, label="Stack_queue O(n)", marker="x")
    plt1.set_xlabel("Input Size")
    plt1.set_ylabel("Execution Time")
    plt1.set_title("Execution Time of Palindrome Algorithms")
    plt1.legend()

    plt2.plot(sizes1, Recursive, label="Recursive O(n)", marker="o")
    plt2.set_xlabel("Input Size")
    plt2.set_ylabel("Execution Time")
    plt2.set_title("Execution Time of Palindrome Algorithms Recursive")
    plt2.legend()

    plt.tight_layout()

    plt.show()
