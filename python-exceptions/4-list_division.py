#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divide element by element two lists up to list_length,
    handling errors as follows:
      - ZeroDivisionError → print "division by 0" and use 0
      - TypeError        → print "wrong type"   and use 0
      - IndexError       → print "out of range" and use 0
    Returns a new list of length list_length with all results.
    """
    results = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            results.append(result)

    return results
