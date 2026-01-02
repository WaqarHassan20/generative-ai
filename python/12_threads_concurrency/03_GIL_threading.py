import threading
import time


def brew_chai():

    print(f"{threading.current_thread().name} Starting to brew chai...")

    count = 0
    for i in range(1_000_000_000):
        count += 1  # Simulate some work

    print(f"{threading.current_thread().name} finished brewing chai!")


if __name__ == "__main__":

    thread1 = threading.Thread(target=brew_chai, name="Chai-Thread-1")
    thread2 = threading.Thread(target=brew_chai, name="Chai-Thread-2")

    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end_time = time.time()

    print(f"Time : {end_time - start_time} s")
    
    
    # GLI : Global Interpreter Lock (GI lock) in python
    # Took this time to run on my machine: Lenovo ThinkPad, model t480, 6th Gen, i5 quad core  
    # Time : 60.21845483779907s # Took around 60 seconds to complete both threads due to GIL