

import threading
import time

#-- Threading.
# It's interesting to note that the CPU have to do some operations
# and it wants to do as fast as possible. So, in this case, numbers
# aren't printed in order due to the sleep command.

def count(n):
    for i in range(1, n+1):
        print(i, "\n")
        time.sleep(0.01)

def count2(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.02)


x = threading.Thread(target = count, args = (10, ))
x.start()

y = threading.Thread(target = count2, args = (10, ))
y.start()

print(f"Thread: {threading.activeCount()}")

print("\n Done")