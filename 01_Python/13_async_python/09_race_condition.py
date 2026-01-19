import threading

chai_stock = 100


def restore_stock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1


threads = [threading.Thread(target=restore_stock) for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()


print("Chai stock : ", chai_stock)

# Chai stock :  500100 : Output on my machine, I don't know why :)