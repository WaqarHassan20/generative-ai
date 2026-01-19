import threading
import requests  # 
import time


urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]


def download_file(url):
    print(f"Starting download from {url}")
    response = requests.get(url)
    print(f"Finished downloading from {url}, SIZE : {len(response.content)} bytes")


threads = []
startTime = time.time()

for url in urls:
    t = threading.Thread(target=download_file, args=(url,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

endTime = time.time()

print(f"Total : {endTime - startTime:.2f} seconds")
