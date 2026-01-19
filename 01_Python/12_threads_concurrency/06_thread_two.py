import time
import threading


def prepare_chai(type_, wait_time):
    print(f"Preparing {type_} chai...")
    time.sleep(wait_time)
    print(f"{type_} chai is ready.")


t1 = threading.Thread(target=prepare_chai, args=("Lemon", 3))
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 4))

if __name__ == "__main__":

    startTime = time.time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    endTime = time.time()

    print(f"Total : {endTime - startTime:.2f} seconds")