import threading
import asyncio
import time
import requests

def check_website(url):
    try:
        response = requests.head(url, timeout=10)
        status_code = response.status_code
        if status_code == 200:
            print(f"{url} is up")
        else:
            print(f"{url} is down")
    except Exception as e:
        print(f"{url} is down: {str(e)}")

async def async_check_website(url):
    try:
        response = await asyncio.wait_for(requests.head(url), timeout=10)
        status_code = response.status_code
        if status_code == 200:
            print(f"{url} is up")
        else:
            print(f"{url} is down")
    except Exception as e:
        print(f"{url} is down: {str(e)}")

def main():
    urls = [
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.sadfafasfasfasf234.com"
    ]

    # Multithreading
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=check_website, args=(url,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f"Multithreading execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
