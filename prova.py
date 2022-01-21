import math
import sys


def foo():
    pass

    try:
        import multiprocessing

        print(multiprocessing.cpu_count())
    except ImportError as exception:
        print(sys.version)
    return math.pi


if name == "__main__":
    foo()
