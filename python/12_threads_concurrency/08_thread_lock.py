import threading
import time

counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1


startTime = time.time()

threads = [threading.Thread(target=increment_counter) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

endTime = time.time()

print(f"Final counter value: {counter}")
print(f"Total : {endTime - startTime:.2f} seconds")

# So it is much faster than the single-threaded version!