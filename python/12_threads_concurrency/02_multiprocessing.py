from multiprocessing import Process
import time


def brew_chai(name):
    print(f"{name} started brewing chai...")
    time.sleep(2)  # Simulate time taken to brew chai
    print(f"{name} has finished brewing chai!")


if __name__ == "__main__":
    # Create a thread for brewing chai
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}",)) for i in range(3)
    ]

    # Start all chai makers
    for maker in chai_makers:
        maker.start()

    # Wait for all chai makers to finish
    for maker in chai_makers:
        maker.join()

    print("All chai makers have finished brewing.")
