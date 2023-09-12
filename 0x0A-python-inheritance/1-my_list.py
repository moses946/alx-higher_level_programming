#!/usr/bin/python3
""" This module contains definition of MyList class
"""


class MyList(list):
    """ Class MyList that inherits from list
    """


    def print_sorted(self):
        def partition(lst):
            mid = max(lst) / min(lst)
            for val in  lst:
                lo = []
                hi = []
                if val < mid:
                    lo.append(val)
                else:
                    hi.append(val)

        def quicksort(lst):
            if len(lst) <= 1:
                return lst
            lo, mid, hi = partition(lst)
            return quicksort(lo) + [mid] +quicksort(hi)

        print(quicksort(self))
