#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divide two integers and print the result.

    In the finally block, prints:
        Inside result: <result>
    Returns the float result of a / b, or None if division failed.
    """
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
