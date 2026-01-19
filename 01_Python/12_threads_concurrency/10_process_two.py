from multiprocessing import Process
import time


def crush_number():
    print("Crushing some number...")
    total = 0
    for i in range(10 ^ 9):
        total += 1
    print("Done ...")


if __name__ == "__main__":

    startTime = time.time()

    processes = [Process(target=crush_number) for _ in range(2)]

    [t.start() for t in processes]
    [t.join() for t in processes]

    print("Total time : ", time.time() - startTime)