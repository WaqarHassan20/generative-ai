import time
import threading


def crush_number():
    print("Crushing some number...")
    total = 0
    for i in range(10 ^ 9):
        total += 1
    print("Done ...")


startTime = time.time()
 
thread = [threading.Thread(target=crush_number) for _ in range(2)]

[t.start() for t in thread]
[t.join() for t in thread]

print("Total time : ", time.time() - startTime)