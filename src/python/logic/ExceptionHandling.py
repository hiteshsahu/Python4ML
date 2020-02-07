"""
Exception Handling
try-> catch->else-> finally
"""
import sys


def divide(x, y):

    try:
        result = x/y
    except ZeroDivisionError as error:
        print("Variable Y is zero: ", format(error))
    except (RuntimeError, TypeError, NameError):
        print("Multiple Error Cached ")
    except:
        print("Generic Error Cached", sys.exc_info()[0])
    else:
        print("Nothing went wrong", result)
    finally:
        print("Finally Called\n")


divide(1, 0)
divide(1, "2")
divide(1, 2+5j)


