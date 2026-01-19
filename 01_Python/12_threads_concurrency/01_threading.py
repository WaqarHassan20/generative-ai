import threading
import time


def take_order():
    for i in range(3):
        print(f"Taking order {i + 1}")
        time.sleep(3)


def prepare_order():
    for i in range(3):
        print(f"Preparing order {i + 1}")
        time.sleep(4)


# Creating threads for taking and preparing orders

order_thread = threading.Thread(target=take_order)
prepare_thread = threading.Thread(target=prepare_order)

# Starting the threads
order_thread.start()
prepare_thread.start()

# Waiting for both threads to complete
order_thread.join()
prepare_thread.join()

print("All orders have been taken and prepared.")