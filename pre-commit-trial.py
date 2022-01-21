"""
Vediamo se va meglio
"""

import math
import sys

"""
Funzione a caso
"""


def foo():
    """
    foo function
    """

    try:
        import multiprocessing

        print(multiprocessing.cpu_count())
    except ImportError as exception:
        print(sys.version)
    return math.pi


"""
Magari adesso gli piace
"""
if name == "__main__":
    """
    Vediamo se funziona questa funzione foo
    """

    foo()
