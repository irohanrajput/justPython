# import time

# def fetch_data(url):
#     print(f"Fetching data from {url}")
#     time.sleep(2)
#     print(f"Data fetched successfully{url}")
    
# def main():
#     start_time = time.time()
#     fetch_data("https://www.google.com")
#     fetch_data("https://www.facebook.com")
#     end_time = time.time()
#     print(f"Time taken: {end_time - start_time}")
    
# if __name__ == "__main__":
#     main()

    
import time
import asyncio

async def fetch_data(url):
    print(f"\n Fetching data from {url}")
    print(f"{url} was started at {time.strftime('%X')}\n")

    await asyncio.sleep(2)
    print(f"Data fetched successfully from {url}")
    
async def main():
    start_time = time.time()
    await asyncio.gather(
        fetch_data("https://www.google.com"),
        fetch_data("https://www.facebook.com")
    )
    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")
    
    
if __name__ == "__main__":
    asyncio.run(main())