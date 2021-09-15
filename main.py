"""
Rafaela Hojda
CMPS 2200  Recitation 1
"""

# the only imports needed are here
import tabulate
import time
###


def linear_search(mylist, key):
    """ done. """
    for i, v in enumerate(mylist):
        if v == key:
            return i
    return -1


def test_linear_search():
    """ done. """
    assert linear_search([1, 2, 3, 4, 5], 5) == 4
    assert linear_search([1, 2, 3, 4, 5], 1) == 0
    assert linear_search([1, 2, 3, 4, 5], 6) == -1


def binary_search(mylist, key):
    """ done. """
    return _binary_search(mylist, key, 0, len(mylist)-1)


def _binary_search(mylist, key, left, right):
    """
    Recursive implementation of binary search.

    Params:
      mylist....list to search
      key.......search key
      left......left index into list to search
      right.....right index into list to search

    Returns:
      index of key in mylist, or -1 if not present.
    """

    if left > right:
        return -1

    middle = (left + right) // 2

    if mylist[middle] == key:
        return middle
    elif key < mylist[middle]:
        return _binary_search(mylist, key, left, middle-1)
    else:
        return _binary_search(mylist, key, middle+1, right)


def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 4, 5], 2)
    assert binary_search([1, 2, 3, 4, 5], 8)

    """
    Worst Case Linear: The last key because its last
    Best Case Linear: The first key because its first

    Worst Case Binary: The middle key
    Best Case Binary: The first and last key 
    """


def time_search(search_fn, mylist, key):
    """
    Return the number of milliseconds to run this
    search function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """

    start_time = time.time()
    search_fn(mylist, key)
    end_time = time.time()
    return (end_time-start_time)*1000


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
    """
    Compare the running time of linear_search and binary_search
    for input sizes as given. The key for each search should be
    -1. The list to search for each size contains the numbers from 0 to n-1,
    sorted in ascending order. 

    You'll use the time_search function to time each call.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """

    size_list = []
    tuple_list = []

    for i in range(len(sizes)):
        key = sizes[i]
        n = int(key)

        for j in range(0, n-1):
            size_list.append(j)

        linear_search_time = time_search(linear_search, size_list, -1)
        binary_search_time = time_search(binary_search, size_list, -1)

        tuple_list.append([n, linear_search_time, binary_search_time])
    return tuple_list


def print_results(results):
    """ done """
    print(tabulate.tabulate(results,
                            headers=['n', 'linear', 'binary'],
                            floatfmt=".3f",
                            tablefmt="github"))


def test_compare_search():
    res = compare_search(sizes=[10, 100])
    print(res)
    assert res[0][0] == 10
    assert res[1][0] == 100
    assert res[0][1] < 1
    assert res[1][1] < 1


print_results(compare_search())

'''
The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. 
Do these theoretical running times match your empirical results? Why or why not?
    Yes because they are still consistent with the running times of O(n) and O(log(n))

'''

'''
Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. 
Suppose you know ahead of time that you will search the same list $k$ times.
    What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? 
        The worst-case complexity would be O(kn)
    For binary search? 
        The worst-case complexity would be O(n^2)
    For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting?
        The values of k that are more efficient to first sort are k > n^2 /(n - log n)
'''
