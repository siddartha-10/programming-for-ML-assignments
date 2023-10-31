import multiprocessing
import random
import time
def merge(l1, l2):
    n1, n2 = len(l1), len(l2)
    i, j = 0, 0
    r = [0] * (n1 + n2)
    while i < n1 and j < n2:
        if l1[i] < l2[j]:
            r[i + j] = l1[i]
            i += 1
        else:
            r[i + j] = l2[j]
            j += 1
    if i < n1:
        while i < n1:
            r[i + j] = l1[i]
            i += 1
    else:
        while j < n2:
            r[i + j] = l2[j]
            j += 1
    return r

def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    k = n // 2
    lower, upper = lst[:k], lst[k:]
    return merge(merge_sort(lower), merge_sort(upper))

def reduce(f, lst, pool):
    if len(lst) == 1:
        return lst[0]

    k = len(lst)
    half = k // 2
    first_half = lst[:half]
    second_half = lst[half:]

    merged_first_half = pool.starmap(f, zip(first_half, second_half))
    return reduce(f, merged_first_half, pool)


def parallel_merge_sort(input_list, num_threads):
    with multiprocessing.Pool(processes=num_threads) as pool:
        k = num_threads
        sublists = [input_list[i * len(input_list) // k:(i + 1) * len(input_list) // k] for i in range(k)]
        sorted_sublists = pool.map(merge_sort, sublists)
        result = reduce(merge, sorted_sublists, pool)
        return result

if __name__ == '__main__':
    input_list = [random.randint(0, 100000) for _ in range(8000000)]

    start_time = time.time()
    sorted_lst = merge_sort(input_list)
    print(f"Sequential merge-sort took {time.time() - start_time} seconds")

    for i in range(2,9,2):
        if i==6:
            continue

        start_time = time.time()
        sorted_lst = parallel_merge_sort(input_list,i)
        print(f"Parallel merge-sort took {time.time() - start_time} seconds using {i} number of threads")