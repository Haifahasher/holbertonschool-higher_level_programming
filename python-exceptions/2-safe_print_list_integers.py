#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of my_list if they are integers,
    skipping silently over any non-integer. Ends with a newline.
    Returns the count of integers actually printed.
    """
    printed_items = 0

    for i in range(x):
        try:
            # attempt to format the ith element as an integer
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            # if it's not an integer, skip silently
            continue
        else:
            # only increment if the print succeeded
            printed_items += 1

    print()
    return printed_items
