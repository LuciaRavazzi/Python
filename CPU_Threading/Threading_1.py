import threading  # new in python 3
import time


# --- Threading


def func(y):
    print("Ran \n")
    time.sleep(y)
    print("Done \n")
    time.sleep(y)
    print("Now done \n")


x = threading.Thread(
    target=func, args=(1,)  # function to thread.  # arguments of the function.
)

# The program starts with the function because it is defined in x.
x.start()
# thanks to the threading module, it is possible to split the
# function line commandas in different steps.
# x.start() execute only one thread.
print(threading.activeCount())

time.sleep(0.1)
print("finally \n ")

# On the basis of the sleep time, the commands are executed not in the sequential
# and original order. I mean, this occurs because the commands don't follow each other
# in the reasoning.
