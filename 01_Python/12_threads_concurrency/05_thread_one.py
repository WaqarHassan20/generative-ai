import time
import threading


def boil_milk():
    print("Boiling milk...")
    time.sleep(2)
    print("Milk boiled.")


def toast_bun():
    print("Toasting bun...")
    time.sleep(2)
    print("Bun toasted.")


if __name__ == "__main__":

    startTime = time.time()

    t1 = threading.Thread(target=boil_milk)
    t2 = threading.Thread(target=toast_bun)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    endTime = time.time()

    print(f"Total : {endTime - startTime:.2f} seconds")