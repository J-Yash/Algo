from random import randint
import time
import matplotlib.pyplot as plt
import math
import sys
sys.setrecursionlimit(10**7)

# Implementation of Insertion Sort Algorithm.


def Insertion_sort(input):
    start_time = time.time()
    for i in range(1, len(input)):
        key = input[i]
        j = i - 1
        while j >= 0 and input[j] > key:
            input[j+1] = input[j]
            j = j - 1
        input[j+1] = key
    end_time = time.time()
    time_taken = end_time - start_time
    return input, time_taken

# Implementation of Merge Sort Algorithm.


def Merge_sort(input, left, right):
    start_time = time.time()
    if left < right:
        mid = math.floor((left + right)/2)
        Merge_sort(input, left, mid)
        Merge_sort(input, mid+1, right)
        Merge(input, left, mid, right)
    end_time = time.time()
    time_taken = end_time - start_time
    return input, time_taken


def Merge(input, left, mid, right):
    n = mid - left + 1
    m = right - mid
    L_list = list()
    R_list = list()
    for i in range(0, n):
        L_list.append(input[left + i])
    for j in range(0, m):
        R_list.append(input[mid + 1 + j])
    i = 0
    j = 0
    k = left
    while i < len(L_list) and j < len(R_list):
        if L_list[i] <= R_list[j]:
            input[k] = L_list[i]
            i += 1
        else:
            input[k] = R_list[j]
            j += 1
        k += 1
    while i < len(L_list):
        input[k] = L_list[i]
        i += 1
        k += 1
    while j < len(R_list):
        input[k] = R_list[j]
        j += 1
        k += 1

# Implementation of Quicksort algorithm.


def Quick_sort(input, p, r):
    start_time = time.time()
    if p < r:
        q = Partition(input, p, r)
        Quick_sort(input, p, q-1)
        Quick_sort(input, q+1, r)
    end_time = time.time()
    time_taken = end_time - start_time
    return input, time_taken


def Partition(input, p, r):
    x = input[r]
    i = p - 1
    for j in range(p, r):
        if input[j] <= x:
            i += 1
            temp = input[i]
            input[i] = input[j]
            input[j] = temp
    temp = input[i+1]
    input[i+1] = input[r]
    input[r] = temp
    return i+1


def Plot_runtimes(ins_runtime_values, merge_runtime_values, quick_runtime_values, plot_file_name):
    """Function to plot input size vs runtimes and save it to a file.
    Input: Takes a list of insertion sort runtimes, a list of merge
    sort runtimes, a list of quick sort runtimes and the name of the
    file (string) to which the plot must be saved.
    Returns: None.
    """
    input_size_values = [5000, 10000, 15000, 20000, 25000, 30000]
    plt.plot(input_size_values, ins_runtime_values, label='Insertion Sort',
             color='blue', linewidth=2, linestyle='dashed',
             marker='.', mfc='k', markersize=10)
    plt.plot(input_size_values, merge_runtime_values, label='Merge Sort',
             color='green', linewidth=2, linestyle='dashed',
             marker='.', mfc='k', markersize=10)
    plt.plot(input_size_values, quick_runtime_values, label='Quick Sort',
             color='red', linewidth=2, linestyle='dashed',
             marker='.', mfc='k', markersize=10)
    plt.xlabel('Size of input (n)')
    plt.ylabel('Time (in seconds)')
    plt.legend()
    plt.savefig(plot_file_name + '.png')  # Save plot to a file.
    plt.close()
    plt.clf()


def Write_I_to_file(unsorted_input, input_file_name):
    """Function to write the unsorted input list to a file.
    Input: Takes a list of unsorted inputs AND a filename to which the list
    must be written.
    Returns: None
    """
    i_file = open(input_file_name + ".txt", 'w')
    i_file.write(str(unsorted_input))
    i_file.close()


def Write_O_to_file(sorted_output, output_file_name):
    """Function to write the sorted output list to a file.
    Input: Takes a list of sorted output AND a filename to which the list
    must be written.
    Returns: None
    """
    o_file = open(output_file_name + ".txt", 'w')
    o_file.write(str(sorted_output))
    o_file.close()


def Write_RT_to_file(runtime, identifier):
    """Function to write the algorithm runtimes to a file.
    Input: Takes a list of runtimes for each input case AND a filename
    to which the list must be written.
    Returns: None
    """
    RT_file = open("Runtimes.txt", 'a')
    RT_file.write(identifier + str(runtime))
    RT_file.close()


def Input_1():
    """Function to implement Input/Plot case 1.
    Input: None
    Returns: None
    """
    size = 5000
    insertion_runtimes = []
    merge_runtimes = []
    quick_runtimes = []
    while size <= 30000:
        ins_time_sum = 0
        merge_time_sum = 0
        quick_time_sum = 0
        for i in range(3):
            unsorted_list = Random_input_generator(size)
            Write_I_to_file(unsorted_list, "Input_ins_1_" + str(size))
            unsorted_list_copy = list(unsorted_list)
            Write_I_to_file(unsorted_list_copy, "Input_merge_1_" + str(size))
            unsorted_list_copy_2 = list(unsorted_list)
            Write_I_to_file(unsorted_list_copy_2, "Input_quick_1_" + str(size))
            insertion_test, time_ins = Insertion_sort(unsorted_list)
            ins_time_sum += time_ins
            Write_O_to_file(insertion_test, "Output_ins_1_" + str(size))
            merge_test, time_merge = Merge_sort(unsorted_list_copy, 0, len(unsorted_list_copy)-1)
            merge_time_sum += time_merge
            Write_O_to_file(merge_test, "Output_merge_1_" + str(size))
            quick_test, time_quick = Quick_sort(unsorted_list_copy_2, 0, len(unsorted_list_copy_2)-1)
            quick_time_sum += time_quick
            Write_O_to_file(quick_test, "Output_quick_1_" + str(size))
        size += 5000
        insertion_runtimes.append(ins_time_sum/3)
        merge_runtimes.append(merge_time_sum/3)
        quick_runtimes.append(quick_time_sum/3)
    Write_RT_to_file(insertion_runtimes, "Ins_input_1: ")
    Write_RT_to_file(merge_runtimes, "Merge_input_1: ")
    Write_RT_to_file(quick_runtimes, "Quick_input_1: ")
    Plot_runtimes(insertion_runtimes, merge_runtimes, quick_runtimes, 'Input_Plot_1')
    print("Case 1 completed!")


def Input_2():
    """Function to implement Input/Plot case 2.
    Input: None
    Returns: None
    """
    size = 5000
    insertion_runtimes = []
    merge_runtimes = []
    quick_runtimes = []
    while size <= 30000:
        ins_time_sum = 0
        merge_time_sum = 0
        quick_time_sum = 0
        for i in range(3):
            unsorted_list = Random_input_generator(size)
            unsorted_list_copy = list(unsorted_list)
            unsorted_list_copy_2 = list(unsorted_list)
            sorted_list = sorted(unsorted_list)
            Write_I_to_file(sorted_list, "Input_ins_2_" + str(size))
            sorted_list_copy = list(sorted_list)
            Write_I_to_file(sorted_list_copy, "Input_merge_2_" + str(size))
            sorted_list_copy_2 = list(sorted_list)
            Write_I_to_file(sorted_list_copy_2, "Input_quick_2_" + str(size))
            insertion_test, time_ins = Insertion_sort(sorted_list)
            ins_time_sum += time_ins
            Write_O_to_file(insertion_test, "Output_ins_2_" + str(size))
            merge_test, time_merge = Merge_sort(sorted_list_copy, 0, len(sorted_list_copy)-1)
            merge_time_sum += time_merge
            Write_O_to_file(merge_test, "Output_merge_2_" + str(size))
            quick_test, time_quick = Quick_sort(sorted_list_copy_2, 0, len(sorted_list_copy_2)-1)
            quick_time_sum += time_quick
            Write_O_to_file(quick_test, "Output_quick_2_" + str(size))
        size += 5000
        insertion_runtimes.append(ins_time_sum/3)
        merge_runtimes.append(merge_time_sum/3)
        quick_runtimes.append(quick_time_sum/3)
    Write_RT_to_file(insertion_runtimes, "Ins_input_2: ")
    Write_RT_to_file(merge_runtimes, "Merge_input_2: ")
    Write_RT_to_file(quick_runtimes, "Quick_input_2: ")
    Plot_runtimes(insertion_runtimes, merge_runtimes, quick_runtimes, 'Input_Plot_2')
    print("Case 2 completed!")


def Input_3():
    """Function to implement Input/Plot case 3.
    Input: None
    Returns: None
    """
    size = 5000
    insertion_runtimes = []
    merge_runtimes = []
    quick_runtimes = []
    while size <= 30000:
        ins_time_sum = 0
        merge_time_sum = 0
        quick_time_sum = 0
        for i in range(3):
            unsorted_list = Random_input_generator(size)
            unsorted_list_copy = list(unsorted_list)
            unsorted_list_copy_2 = list(unsorted_list)
            sorted_list = sorted(unsorted_list, reverse=True)
            Write_I_to_file(sorted_list, "Input_ins_3_" + str(size))
            sorted_list_copy = list(sorted_list)
            Write_I_to_file(sorted_list_copy, "Input_merge_3_" + str(size))
            sorted_list_copy_2 = list(sorted_list)
            Write_I_to_file(sorted_list_copy_2, "Input_quick_3_" + str(size))
            insertion_test, time_ins = Insertion_sort(sorted_list)
            ins_time_sum += time_ins
            Write_O_to_file(insertion_test, "Output_ins_3_" + str(size))
            merge_test, time_merge = Merge_sort(sorted_list_copy, 0, len(sorted_list_copy)-1)
            merge_time_sum += time_merge
            Write_O_to_file(merge_test, "Output_merge_3_" + str(size))
            quick_test, time_quick = Quick_sort(sorted_list_copy_2, 0, len(sorted_list_copy_2)-1)
            quick_time_sum += time_quick
            Write_O_to_file(quick_test, "Output_quick_3_" + str(size))
        size += 5000
        insertion_runtimes.append(ins_time_sum/3)
        merge_runtimes.append(merge_time_sum/3)
        quick_runtimes.append(quick_time_sum/3)
    Write_RT_to_file(insertion_runtimes, "Ins_input_3: ")
    Write_RT_to_file(merge_runtimes, "Merge_input_3: ")
    Write_RT_to_file(quick_runtimes, "Quick_input_3: ")
    Plot_runtimes(insertion_runtimes, merge_runtimes, quick_runtimes, 'Input_Plot_3')
    print("Case 3 completed!")


def Input_4():
    """Function to implement Input/Plot case 4.
    Input: None
    Returns: None
    """
    size = 5000
    insertion_runtimes = []
    merge_runtimes = []
    quick_runtimes = []
    while size <= 30000:
        ins_time_sum = 0
        merge_time_sum = 0
        quick_time_sum = 0
        for i in range(3):
            unsorted_list = Random_input_generator(size)
            unsorted_list_copy = list(unsorted_list)
            sorted_list = sorted(unsorted_list)
            sorted_list_copy = list(sorted_list)
            sorted_list_copy_2 = list(sorted_list)
            for k in range(50):
                i = randint(0, size)
                j = randint(0, size)
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[j]
                sorted_list[j] = temp
                temp = sorted_list_copy[i]
                sorted_list_copy[i] = sorted_list_copy[j]
                sorted_list_copy[j] = temp
                temp = sorted_list_copy_2[i]
                sorted_list_copy_2[i] = sorted_list_copy_2[j]
                sorted_list_copy_2[j] = temp
            Write_I_to_file(sorted_list, "Input_ins_4_" + str(size))
            Write_I_to_file(sorted_list_copy, "Input_merge_4_" + str(size))
            Write_I_to_file(sorted_list_copy_2, "Input_quick_4_" + str(size))
            insertion_test, time_ins = Insertion_sort(sorted_list)
            ins_time_sum += time_ins
            Write_O_to_file(insertion_test, "Output_ins_4_" + str(size))
            merge_test, time_merge = Merge_sort(sorted_list_copy, 0, len(sorted_list_copy)-1)
            merge_time_sum += time_merge
            Write_O_to_file(merge_test, "Output_merge_4_" + str(size))
            quick_test, time_quick = Quick_sort(sorted_list_copy_2)
            quick_time_sum += time_quick
            Write_O_to_file(quick_test, "Output_quick_4_" + str(size))
        size += 5000
        insertion_runtimes.append(ins_time_sum/3)
        merge_runtimes.append(merge_time_sum/3)
        quick_runtimes.append(quick_time_sum/3)
    Write_RT_to_file(insertion_runtimes, "Ins_input_4: ")
    Write_RT_to_file(merge_runtimes, "Merge_input_4: ")
    Write_RT_to_file(quick_runtimes, "Quick_input_4: ")
    Plot_runtimes(insertion_runtimes, merge_runtimes, quick_runtimes, 'Input_Plot_4')
    print("Case 4 completed!")


def Input_5():
    """Function to implement Input/Plot case 5.
    Input: None
    Returns: None
    """
    size = 50
    input_list = []
    for i in range(100000):
        unsorted_list = Random_input_generator(size)
        input_list.append(unsorted_list)
    input_list_copy = list(input_list)
    input_list_copy_2 = list(input_list)
    Write_I_to_file(input_list, "Input_ins_5_" + str(size))
    Write_I_to_file(input_list_copy, "Input_merge_5_" + str(size))
    Write_I_to_file(input_list_copy_2, "Input_quick_5_" + str(size))
    total_ins_time = 0
    total_merge_time = 0
    total_quick_time = 0
    for i in range(100000):
        insertion_test, time_ins = Insertion_sort(input_list[i])
        total_ins_time += time_ins
        merge_test, time_merge = Merge_sort(input_list_copy[i])
        total_merge_time += time_merge
        quick_test, time_quick = Quick_sort(input_list_copy_2[i])
        total_quick_time += time_quick
    Write_O_to_file(insertion_test, "Output_ins_5_" + str(size))
    Write_O_to_file(merge_test, "Output_merge_5_" + str(size))
    Write_O_to_file(quick_test, "Output_quick_5_" + str(size))
    Write_RT_to_file(total_ins_time, "Ins_Total_time_input_5: ")
    Write_RT_to_file(total_merge_time, "Merge_Total_time_input_5: ")
    Write_RT_to_file(total_quick_time, "Quick_Total_time_input_5: ")
    print("Case 5 completed!")


def Random_input_generator(size_n):
    """Function to generate a list of uniformly random integers.
    Input: Takes an integer value for size of the list
    Returns: A list of uniformly random integers.
    """
    random_values = []
    for _ in range(size_n):
        random_values.append(randint(1, size_n))
    return random_values


if __name__ == '__main__':
    # Input_1()
    Input_2()
    # Input_3()
    # Input_4()
    # Input_5()
