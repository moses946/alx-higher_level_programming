#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except Exception:
        if Exception == ZeroDivisionError:
            result = None
    finally:
        print("Inside result: {}\n".format(result))
        print("{} / {} = {}".format(a, b, result))