from multiprocessing import Process, Queue


def prepare_chai(queue):
    queue.put("Chai is ready!")


if __name__ == "__main__":

    que = Queue()

    process = Process(target=prepare_chai, args=(que,))

    process.start()
    process.join()

    print("Message is : ", que.get())
