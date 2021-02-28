import random
import time

def generate_random_integer_list(list_size):

    a_list = []
    for i in range(list_size):
        num = random.randint(0,list_size)
        a_list.append(num)

    return a_list

def sequential_search(a_list):
    pos = 0
    found = False

    while pos < len(a_list) and not found:

        if a_list[pos] == -1:
            found = True
        else:
            pos = pos + 1
    return found

def ordered_sequential_search(a_list):
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == -1:
            found = True

        elif a_list[pos] > -1:
            stop = True
        else:
            pos = pos + 1
    return found

def binary_search_iterative(a_list):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == -1:
            found = True
        elif -1 < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found

def binary_search_recursive(a_list):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == -1:
        return True
    elif -1 < a_list[midpoint]:
        return binary_search_recursive(a_list[:midpoint])
    else:
        return binary_search_recursive(a_list[midpoint + 1:])

if __name__ == "__main__":

    list_sizes = [500, 1000, 5000]

    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            a_list = generate_random_integer_list(list_size)
            start = time.time()
            sequential_search(a_list)
            end = time.time()
            sorted_time = end - start
            total_time += sorted_time
            avg_time = total_time / 100
        print(f"Sequential Search took {avg_time:0.8f} in list sizes {list_size}.")
    print("\n")

    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            a_list = generate_random_integer_list(list_size)
            start = time.time()
            ordered_sequential_search(sorted(a_list))
            end = time.time()
            sorted_time = end - start
            total_time += sorted_time
            avg_time = total_time / 100
        print(f"Ordered Sequential Search took {avg_time:0.8f} in list sizes {list_size}.")
    print("\n")

    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            a_list = generate_random_integer_list(list_size)
            start = time.time()
            binary_search_iterative(sorted(a_list))
            end = time.time()
            sorted_time = end - start
            total_time += sorted_time
            avg_time = total_time / 100
        print(f"Binary Search Iterative took {avg_time:0.8f} in list sizes {list_size}.")
    print("\n")

    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            a_list = generate_random_integer_list(list_size)
            start = time.time()
            binary_search_recursive(sorted(a_list))
            end = time.time()
            sorted_time = end - start
            total_time += sorted_time
            avg_time = total_time / 100
        print(f"Binary Search Recursive took {avg_time:0.8f} in list sizes {list_size}.")