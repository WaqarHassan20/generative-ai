from multiprocessing import Process
import time


def brew_chai():

    print("Start counting...")

    count = 0
    for i in range(1_000_000_000):
        count += 1  # Simulate some work

    print(f"Finished counting!")


if __name__ == "__main__":

    process1 = Process(target=brew_chai)
    process2 = Process(target=brew_chai)

    start_time = time.time()
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    end_time = time.time()

    print(f"Time : {end_time - start_time} s")