import random
import time

def generate_random_integer_list(list_size):

    a_list = []
    for i in range(list_size):
        num = random.randint(0,list_size)
        a_list.append(num)

    return a_list

def insertion_sort(a_list):


    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            a_list[position] = current_value
    return a_list

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value
    return a_list

def python_sort(a_list):
    a_list.sort()
    return a_list

if __name__ == "__main__":

    list_sizes = [500, 1000, 5000]

    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            a_list = generate_random_integer_list(list_size)
            start = time.time()

            insertion_sort(a_list)

            end = time.time()
            sorted_time = end - start
            total_time += sorted_time
            avg_time = total_time / 100
        print(f"insertion sort took {avg_time:0.8f} in list sizes {list_size}.")

    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            a_list = generate_random_integer_list(list_size)
            start = time.time()

            shell_sort(a_list)

            end = time.time()
            sorted_time = end - start
            total_time += sorted_time
            avg_time = total_time / 100
        print(f"Shell sort took {avg_time:0.8f} in list sizes {list_size}.")

    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            a_list = generate_random_integer_list(list_size)
            start = time.time()

            python_sort(a_list)

            end = time.time()
            sorted_time = end - start
            total_time += sorted_time
            avg_time = total_time / 100
        print(f"Python sort took {avg_time:0.8f} in list sizes {list_size}.")