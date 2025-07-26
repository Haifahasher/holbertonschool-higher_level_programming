#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print up to x elements of my_list and return how many were printed."""
    count = 0
    for i in range(x):
        try:
            # attempt to print the element at index i
            print("{}".format(my_list[i]), end="")
        except Exception:
            # if accessing my_list[i] fails (IndexError), stop the loop
            break
        else:
            # only increment when the print succeeded
            count += 1
    print()      # finish with a newline
    return count
