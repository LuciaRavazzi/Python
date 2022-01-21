import threading
import time

ls = []


# --- Threading.
# In this case, without join operations, the list would be printed
# after the end of the append operation and some number would be missed.
# The join operation allows to wait all the command of a specific thread to
# be completely executed.

# Consecutive joins return: [1, 1, 2, 3, 4, 5, 2, 3, 4, 5]
# x.join() -> y.join(): [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


def count(n):
    for i in range(1, n + 1):
        ls.append(i)
        time.sleep(0.5)


def count2(n):
    for i in range(1, n + 1):
        ls.append(i)


x = threading.Thread(target=count, args=(5,))
x.start()

x.join()

y = threading.Thread(target=count2, args=(5,))
y.start()

y.join()

print(ls)
